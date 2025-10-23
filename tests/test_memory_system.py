"""
Test suite for AI Live Genie Memory and Streaming Data systems.
"""

import unittest
import os
import sys
import json
import shutil

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from ai_live_genie import ConversationalMemory, LongTermMemory, GoalsManager, MemoryManager, StreamingPlatformData


class TestConversationalMemory(unittest.TestCase):
    """Test conversational memory functionality."""
    
    def setUp(self):
        self.memory = ConversationalMemory(max_history=5)
    
    def test_add_message(self):
        """Test adding messages to memory."""
        self.memory.add_message("user", "Hello")
        self.assertEqual(len(self.memory.get_history()), 1)
        self.assertEqual(self.memory.get_history()[0]["content"], "Hello")
    
    def test_max_history_limit(self):
        """Test that history respects max limit."""
        for i in range(10):
            self.memory.add_message("user", f"Message {i}")
        self.assertEqual(len(self.memory.get_history()), 5)
    
    def test_get_history_last_n(self):
        """Test retrieving last N messages."""
        for i in range(5):
            self.memory.add_message("user", f"Message {i}")
        last_two = self.memory.get_history(last_n=2)
        self.assertEqual(len(last_two), 2)
        self.assertEqual(last_two[-1]["content"], "Message 4")
    
    def test_clear(self):
        """Test clearing memory."""
        self.memory.add_message("user", "Test")
        self.memory.clear()
        self.assertEqual(len(self.memory.get_history()), 0)


class TestLongTermMemory(unittest.TestCase):
    """Test long-term memory functionality."""
    
    def setUp(self):
        self.test_file = "/tmp/test_long_term_memory.json"
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        self.memory = LongTermMemory(storage_path=self.test_file)
    
    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
    
    def test_store_and_retrieve_fact(self):
        """Test storing and retrieving facts."""
        self.memory.store_fact("Test fact", category="test")
        facts = self.memory.retrieve_facts(category="test")
        self.assertEqual(len(facts), 1)
        self.assertEqual(facts[0]["content"], "Test fact")
    
    def test_store_and_retrieve_preference(self):
        """Test storing and retrieving preferences."""
        self.memory.store_preference("color", "blue")
        color = self.memory.retrieve_preference("color")
        self.assertEqual(color, "blue")
    
    def test_store_and_retrieve_entity(self):
        """Test storing and retrieving entities."""
        self.memory.store_entity("test_channel", {"platform": "YouTube", "subs": 1000})
        entity = self.memory.retrieve_entity("test_channel")
        self.assertEqual(entity["platform"], "YouTube")
        self.assertEqual(entity["subs"], 1000)
    
    def test_search_memory(self):
        """Test searching through memory."""
        self.memory.store_fact("YouTube streaming is fun", category="test")
        self.memory.store_entity("yt_channel", {"name": "TestChannel"})
        results = self.memory.search_memory("youtube")
        self.assertGreater(len(results), 0)
    
    def test_persistence(self):
        """Test that data persists across instances."""
        self.memory.store_preference("persist_test", "value123")
        
        # Create new instance
        new_memory = LongTermMemory(storage_path=self.test_file)
        value = new_memory.retrieve_preference("persist_test")
        self.assertEqual(value, "value123")


class TestGoalsManager(unittest.TestCase):
    """Test goals management functionality."""
    
    def setUp(self):
        self.test_file = "/tmp/test_goals.json"
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        self.goals = GoalsManager(storage_path=self.test_file)
    
    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
    
    def test_add_goal(self):
        """Test adding a goal."""
        goal = self.goals.add_goal("Test Goal", "Description", priority="high")
        self.assertIsNotNone(goal)
        self.assertEqual(goal["title"], "Test Goal")
        self.assertEqual(goal["priority"], "high")
    
    def test_update_goal_progress(self):
        """Test updating goal progress."""
        goal = self.goals.add_goal("Test Goal", "Description")
        result = self.goals.update_goal_progress(goal["id"], 50)
        self.assertTrue(result)
        updated_goal = self.goals.get_goal_by_id(goal["id"])
        self.assertEqual(updated_goal["progress"], 50)
    
    def test_complete_goal(self):
        """Test completing a goal."""
        goal = self.goals.add_goal("Test Goal", "Description")
        result = self.goals.complete_goal(goal["id"])
        self.assertTrue(result)
        self.assertEqual(len(self.goals.get_active_goals()), 0)
        self.assertEqual(len(self.goals.goals["completed_goals"]), 1)
    
    def test_add_milestone(self):
        """Test adding milestones."""
        goal = self.goals.add_goal("Test Goal", "Description")
        result = self.goals.add_milestone(goal["id"], "First milestone")
        self.assertTrue(result)
        updated_goal = self.goals.get_goal_by_id(goal["id"])
        self.assertEqual(len(updated_goal["milestones"]), 1)


class TestStreamingPlatformData(unittest.TestCase):
    """Test streaming platform data functionality."""
    
    def setUp(self):
        self.test_file = "/tmp/test_streaming_data.json"
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        self.streaming = StreamingPlatformData(storage_path=self.test_file)
    
    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
    
    def test_get_platform_data(self):
        """Test getting platform data."""
        youtube_data = self.streaming.get_platform_data("youtube")
        self.assertIsNotNone(youtube_data)
        self.assertEqual(youtube_data["name"], "YouTube")
        self.assertIn("payout_per_1000_views", youtube_data)
    
    def test_get_all_platforms(self):
        """Test getting all platforms."""
        platforms = self.streaming.get_all_platforms()
        self.assertGreater(len(platforms), 0)
        self.assertIn("youtube", platforms)
        self.assertIn("twitch", platforms)
    
    def test_calculate_earnings(self):
        """Test earnings calculation."""
        earnings = self.streaming.calculate_earnings("youtube", 10000)
        self.assertIn("estimated_earnings", earnings)
        self.assertIn("min", earnings["estimated_earnings"])
        self.assertIn("max", earnings["estimated_earnings"])
        self.assertIn("average", earnings["estimated_earnings"])
    
    def test_calculate_subscribers_from_views(self):
        """Test subscriber calculation."""
        subs = self.streaming.calculate_subscribers_from_views("youtube", 10000, "average")
        self.assertIsInstance(subs, int)
        self.assertGreater(subs, 0)
    
    def test_compare_platforms(self):
        """Test platform comparison."""
        comparison = self.streaming.compare_platforms(50000)
        self.assertGreater(len(comparison), 0)
        # Should be sorted by average earnings
        if len(comparison) > 1:
            self.assertGreaterEqual(
                comparison[0]["estimated_earnings"]["average"],
                comparison[1]["estimated_earnings"]["average"]
            )
    
    def test_get_monetization_requirements(self):
        """Test getting monetization requirements."""
        requirements = self.streaming.get_monetization_requirements("youtube")
        self.assertIsNotNone(requirements)
        self.assertIn("subscribers", requirements)
    
    def test_get_earning_factors(self):
        """Test getting earning factors."""
        factors = self.streaming.get_earning_factors("youtube")
        self.assertIsNotNone(factors)
        self.assertIsInstance(factors, list)
        self.assertGreater(len(factors), 0)
    
    def test_add_custom_platform(self):
        """Test adding custom platform."""
        custom_data = {
            "name": "CustomPlatform",
            "payout_per_1000_views": {
                "min": 1.0,
                "max": 2.0,
                "average": 1.5,
                "currency": "USD"
            }
        }
        self.streaming.add_custom_platform("custom", custom_data)
        retrieved = self.streaming.get_platform_data("custom")
        self.assertIsNotNone(retrieved)
        self.assertEqual(retrieved["name"], "CustomPlatform")


class TestMemoryManager(unittest.TestCase):
    """Test integrated memory manager."""
    
    def setUp(self):
        self.test_dir = "/tmp/test_memory_manager"
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
        os.makedirs(self.test_dir)
        self.manager = MemoryManager(data_dir=self.test_dir)
    
    def tearDown(self):
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
    
    def test_process_interaction(self):
        """Test processing an interaction."""
        self.manager.process_interaction("Hello", "Hi there!")
        history = self.manager.conversational.get_history()
        self.assertEqual(len(history), 2)
        self.assertEqual(history[0]["role"], "user")
        self.assertEqual(history[1]["role"], "assistant")
    
    def test_get_full_context(self):
        """Test getting full context."""
        self.manager.process_interaction("Test", "Response")
        self.manager.long_term.store_fact("Test fact")
        self.manager.goals.add_goal("Test goal", "Description")
        
        context = self.manager.get_full_context()
        self.assertIn("conversation_history", context)
        self.assertIn("recent_facts", context)
        self.assertIn("active_goals", context)
        self.assertIn("preferences", context)


def run_tests():
    """Run all tests."""
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add all test classes
    suite.addTests(loader.loadTestsFromTestCase(TestConversationalMemory))
    suite.addTests(loader.loadTestsFromTestCase(TestLongTermMemory))
    suite.addTests(loader.loadTestsFromTestCase(TestGoalsManager))
    suite.addTests(loader.loadTestsFromTestCase(TestStreamingPlatformData))
    suite.addTests(loader.loadTestsFromTestCase(TestMemoryManager))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    return result.wasSuccessful()


if __name__ == "__main__":
    success = run_tests()
    exit(0 if success else 1)
