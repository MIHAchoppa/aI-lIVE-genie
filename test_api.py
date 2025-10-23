"""
Test suite for AI Live Genie REST API.
"""

import unittest
import json
import os
import shutil
from api_server import app


class TestAPIServer(unittest.TestCase):
    """Test API server endpoints."""
    
    @classmethod
    def setUpClass(cls):
        """Set up test environment."""
        # Set test API key
        os.environ['AI_GENIE_API_KEY'] = 'test-api-key'
        
    def setUp(self):
        """Set up test client and test data directory."""
        self.app = app
        self.app.config['TESTING'] = True
        
        # Create test data directory
        self.test_dir = "/tmp/test_api_data"
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
        os.makedirs(self.test_dir)
        
        # Configure app to use test data directory
        self.app.config['DATA_DIR'] = self.test_dir
        
        # Clear any cached instances
        if hasattr(self.app, 'memory_manager'):
            delattr(self.app, 'memory_manager')
        if hasattr(self.app, 'streaming_data'):
            delattr(self.app, 'streaming_data')
        
        self.client = self.app.test_client()
        self.api_key = 'test-api-key'
    
    def tearDown(self):
        """Clean up test data."""
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
    
    def get_headers(self):
        """Get request headers with API key."""
        return {'X-API-Key': self.api_key, 'Content-Type': 'application/json'}
    
    # ========== Health Check Tests ==========
    
    def test_health_check(self):
        """Test health check endpoint."""
        response = self.client.get('/health')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'healthy')
    
    # ========== Authentication Tests ==========
    
    def test_auth_missing_key(self):
        """Test endpoint without API key."""
        response = self.client.post('/api/conversation/message',
                                    json={'role': 'user', 'content': 'test'})
        self.assertEqual(response.status_code, 401)
    
    def test_auth_invalid_key(self):
        """Test endpoint with invalid API key."""
        headers = {'X-API-Key': 'wrong-key', 'Content-Type': 'application/json'}
        response = self.client.post('/api/conversation/message',
                                    headers=headers,
                                    json={'role': 'user', 'content': 'test'})
        self.assertEqual(response.status_code, 401)
    
    def test_auth_valid_key_header(self):
        """Test endpoint with valid API key in header."""
        response = self.client.post('/api/conversation/message',
                                    headers=self.get_headers(),
                                    json={'role': 'user', 'content': 'test'})
        self.assertEqual(response.status_code, 200)
    
    def test_auth_valid_key_query(self):
        """Test endpoint with valid API key in query parameter."""
        response = self.client.post(f'/api/conversation/message?api_key={self.api_key}',
                                    headers={'Content-Type': 'application/json'},
                                    json={'role': 'user', 'content': 'test'})
        self.assertEqual(response.status_code, 200)
    
    # ========== Conversational Memory Tests ==========
    
    def test_add_message(self):
        """Test adding a message."""
        response = self.client.post('/api/conversation/message',
                                    headers=self.get_headers(),
                                    json={'role': 'user', 'content': 'Hello'})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'success')
    
    def test_add_message_missing_fields(self):
        """Test adding message with missing fields."""
        response = self.client.post('/api/conversation/message',
                                    headers=self.get_headers(),
                                    json={'role': 'user'})
        self.assertEqual(response.status_code, 400)
    
    def test_process_interaction(self):
        """Test processing interaction."""
        response = self.client.post('/api/conversation/interaction',
                                    headers=self.get_headers(),
                                    json={
                                        'user_input': 'Hello',
                                        'assistant_response': 'Hi there!'
                                    })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'success')
    
    def test_get_conversation_history(self):
        """Test getting conversation history."""
        # Add some messages first
        self.client.post('/api/conversation/message',
                        headers=self.get_headers(),
                        json={'role': 'user', 'content': 'Hello'})
        
        response = self.client.get('/api/conversation/history',
                                  headers=self.get_headers())
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('history', data)
        self.assertIsInstance(data['history'], list)
    
    def test_get_conversation_summary(self):
        """Test getting conversation summary."""
        response = self.client.get('/api/conversation/summary',
                                  headers=self.get_headers())
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('summary', data)
    
    def test_clear_conversation(self):
        """Test clearing conversation."""
        response = self.client.post('/api/conversation/clear',
                                   headers=self.get_headers())
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'success')
    
    # ========== Long-term Memory Tests ==========
    
    def test_store_fact(self):
        """Test storing a fact."""
        response = self.client.post('/api/memory/fact',
                                   headers=self.get_headers(),
                                   json={'fact': 'Test fact', 'category': 'test'})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'success')
    
    def test_retrieve_facts(self):
        """Test retrieving facts."""
        # Store a fact first
        self.client.post('/api/memory/fact',
                        headers=self.get_headers(),
                        json={'fact': 'Test fact', 'category': 'test'})
        
        response = self.client.get('/api/memory/fact',
                                  headers=self.get_headers())
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('facts', data)
    
    def test_store_preference(self):
        """Test storing a preference."""
        response = self.client.post('/api/memory/preference',
                                   headers=self.get_headers(),
                                   json={'key': 'color', 'value': 'blue'})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'success')
    
    def test_retrieve_preference(self):
        """Test retrieving a preference."""
        # Store preference first
        self.client.post('/api/memory/preference',
                        headers=self.get_headers(),
                        json={'key': 'color', 'value': 'blue'})
        
        response = self.client.get('/api/memory/preference/color',
                                  headers=self.get_headers())
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['value'], 'blue')
    
    def test_store_entity(self):
        """Test storing an entity."""
        response = self.client.post('/api/memory/entity',
                                   headers=self.get_headers(),
                                   json={
                                       'entity_name': 'channel',
                                       'entity_data': {'platform': 'YouTube'}
                                   })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'success')
    
    def test_retrieve_entity(self):
        """Test retrieving an entity."""
        # Store entity first
        self.client.post('/api/memory/entity',
                        headers=self.get_headers(),
                        json={
                            'entity_name': 'channel',
                            'entity_data': {'platform': 'YouTube'}
                        })
        
        response = self.client.get('/api/memory/entity/channel',
                                  headers=self.get_headers())
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['data']['platform'], 'YouTube')
    
    def test_search_memory(self):
        """Test searching memory."""
        # Store some data first
        self.client.post('/api/memory/fact',
                        headers=self.get_headers(),
                        json={'fact': 'YouTube is great', 'category': 'test'})
        
        response = self.client.get('/api/memory/search?query=youtube',
                                  headers=self.get_headers())
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('results', data)
    
    # ========== Goals Management Tests ==========
    
    def test_add_goal(self):
        """Test adding a goal."""
        response = self.client.post('/api/goals',
                                   headers=self.get_headers(),
                                   json={
                                       'title': 'Test Goal',
                                       'description': 'Test description',
                                       'priority': 'high'
                                   })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'success')
        self.assertIn('goal', data)
    
    def test_get_goals(self):
        """Test getting goals."""
        response = self.client.get('/api/goals',
                                  headers=self.get_headers())
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('goals', data)
    
    def test_get_goal_by_id(self):
        """Test getting a specific goal."""
        # Create a goal first
        create_response = self.client.post('/api/goals',
                                          headers=self.get_headers(),
                                          json={
                                              'title': 'Test Goal',
                                              'description': 'Test description'
                                          })
        goal_id = json.loads(create_response.data)['goal']['id']
        
        response = self.client.get(f'/api/goals/{goal_id}',
                                  headers=self.get_headers())
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('goal', data)
    
    def test_update_goal_progress(self):
        """Test updating goal progress."""
        # Create a goal first
        create_response = self.client.post('/api/goals',
                                          headers=self.get_headers(),
                                          json={
                                              'title': 'Test Goal',
                                              'description': 'Test description'
                                          })
        goal_id = json.loads(create_response.data)['goal']['id']
        
        response = self.client.put(f'/api/goals/{goal_id}/progress',
                                  headers=self.get_headers(),
                                  json={'progress': 50})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'success')
    
    def test_complete_goal(self):
        """Test completing a goal."""
        # Create a goal first
        create_response = self.client.post('/api/goals',
                                          headers=self.get_headers(),
                                          json={
                                              'title': 'Test Goal',
                                              'description': 'Test description'
                                          })
        goal_id = json.loads(create_response.data)['goal']['id']
        
        response = self.client.post(f'/api/goals/{goal_id}/complete',
                                   headers=self.get_headers())
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'success')
    
    def test_add_milestone(self):
        """Test adding a milestone."""
        # Create a goal first
        create_response = self.client.post('/api/goals',
                                          headers=self.get_headers(),
                                          json={
                                              'title': 'Test Goal',
                                              'description': 'Test description'
                                          })
        goal_id = json.loads(create_response.data)['goal']['id']
        
        response = self.client.post(f'/api/goals/{goal_id}/milestone',
                                   headers=self.get_headers(),
                                   json={'milestone': 'First milestone'})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'success')
    
    # ========== Streaming Platform Data Tests ==========
    
    def test_get_platforms(self):
        """Test getting all platforms."""
        response = self.client.get('/api/streaming/platforms')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('platforms', data)
        self.assertIsInstance(data['platforms'], list)
    
    def test_get_platform_data(self):
        """Test getting platform data."""
        response = self.client.get('/api/streaming/platform/youtube')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['platform'], 'youtube')
        self.assertIn('data', data)
    
    def test_calculate_earnings(self):
        """Test calculating earnings."""
        response = self.client.get('/api/streaming/earnings?platform=youtube&views=10000')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['platform'], 'youtube')
        self.assertIn('estimated_earnings', data)
    
    def test_calculate_earnings_missing_params(self):
        """Test calculating earnings with missing parameters."""
        response = self.client.get('/api/streaming/earnings?platform=youtube')
        self.assertEqual(response.status_code, 400)
    
    def test_compare_platforms(self):
        """Test comparing platforms."""
        response = self.client.get('/api/streaming/compare?views=50000')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('comparison', data)
        self.assertIsInstance(data['comparison'], list)
    
    def test_calculate_subscribers(self):
        """Test calculating subscribers."""
        response = self.client.get('/api/streaming/subscribers?platform=youtube&views=10000')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('expected_subscribers', data)
    
    def test_get_conversion_rates(self):
        """Test getting conversion rates."""
        response = self.client.get('/api/streaming/conversion-rates?type=view_to_subscriber')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('rates', data)
    
    def test_get_requirements(self):
        """Test getting monetization requirements."""
        response = self.client.get('/api/streaming/requirements/youtube')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['platform'], 'youtube')
        self.assertIn('requirements', data)
    
    def test_get_factors(self):
        """Test getting earning factors."""
        response = self.client.get('/api/streaming/factors/youtube')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['platform'], 'youtube')
        self.assertIn('factors', data)
    
    # ========== Context Tests ==========
    
    def test_get_full_context(self):
        """Test getting full context."""
        response = self.client.get('/api/context',
                                  headers=self.get_headers())
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('conversation_history', data)
        self.assertIn('recent_facts', data)
        self.assertIn('active_goals', data)
        self.assertIn('preferences', data)
    
    # ========== Error Handling Tests ==========
    
    def test_404_error(self):
        """Test 404 error handling."""
        response = self.client.get('/api/nonexistent')
        self.assertEqual(response.status_code, 404)
        data = json.loads(response.data)
        self.assertIn('error', data)


def run_tests():
    """Run all API tests."""
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    suite.addTests(loader.loadTestsFromTestCase(TestAPIServer))
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    return result.wasSuccessful()


if __name__ == "__main__":
    success = run_tests()
    exit(0 if success else 1)
