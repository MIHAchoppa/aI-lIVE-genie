"""
REST API Server for AI Live Genie
Provides HTTP endpoints for memory management and streaming data access.
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
from functools import wraps
import os
from .memory_manager import MemoryManager
from .streaming_data import StreamingPlatformData

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests

# Initialize memory and streaming data systems
# Use a factory pattern to allow for testing with different data directories
def get_memory_manager():
    """Get or create memory manager instance."""
    if not hasattr(app, 'memory_manager'):
        data_dir = app.config.get('DATA_DIR', './data')
        app.memory_manager = MemoryManager(data_dir=data_dir)
    return app.memory_manager

def get_streaming_data():
    """Get or create streaming data instance."""
    if not hasattr(app, 'streaming_data'):
        app.streaming_data = StreamingPlatformData()
    return app.streaming_data


def require_api_key(f):
    """Decorator to require API key authentication."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Get API key from environment each time for testing flexibility
        api_key_expected = os.environ.get('AI_GENIE_API_KEY', 'dev-key-change-in-production')
        api_key = request.headers.get('X-API-Key') or request.args.get('api_key')
        if not api_key or api_key != api_key_expected:
            return jsonify({"error": "Invalid or missing API key"}), 401
        return f(*args, **kwargs)
    return decorated_function


# Health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({"status": "healthy", "service": "AI Live Genie API"})


# ========== Conversational Memory Endpoints ==========

@app.route('/api/conversation/message', methods=['POST'])
@require_api_key
def add_conversation_message():
    """Add a message to conversational memory."""
    data = request.get_json()
    role = data.get('role')
    content = data.get('content')
    metadata = data.get('metadata', {})
    
    if not role or not content:
        return jsonify({"error": "Role and content are required"}), 400
    
    memory_manager = get_memory_manager()
    memory_manager.conversational.add_message(role, content, metadata)
    return jsonify({"status": "success", "message": "Message added"})


@app.route('/api/conversation/interaction', methods=['POST'])
@require_api_key
def process_interaction():
    """Process a complete user-assistant interaction."""
    data = request.get_json()
    user_input = data.get('user_input')
    assistant_response = data.get('assistant_response')
    
    if not user_input or not assistant_response:
        return jsonify({"error": "Both user_input and assistant_response are required"}), 400
    
    memory_manager = get_memory_manager()
    memory_manager.process_interaction(user_input, assistant_response)
    return jsonify({"status": "success", "message": "Interaction processed"})


@app.route('/api/conversation/history', methods=['GET'])
@require_api_key
def get_conversation_history():
    """Get conversation history."""
    last_n = request.args.get('last_n', type=int)
    memory_manager = get_memory_manager()
    history = memory_manager.conversational.get_history(last_n=last_n)
    return jsonify({"history": history})


@app.route('/api/conversation/summary', methods=['GET'])
@require_api_key
def get_conversation_summary():
    """Get conversation context summary."""
    memory_manager = get_memory_manager()
    summary = memory_manager.conversational.get_context_summary()
    return jsonify({"summary": summary})


@app.route('/api/conversation/clear', methods=['POST'])
@require_api_key
def clear_conversation():
    """Clear conversation history."""
    memory_manager = get_memory_manager()
    memory_manager.conversational.clear()
    return jsonify({"status": "success", "message": "Conversation history cleared"})


# ========== Long-term Memory Endpoints ==========

@app.route('/api/memory/fact', methods=['POST'])
@require_api_key
def store_fact():
    """Store a fact in long-term memory."""
    data = request.get_json()
    fact = data.get('fact')
    category = data.get('category', 'general')
    
    if not fact:
        return jsonify({"error": "Fact is required"}), 400
    
    memory_manager = get_memory_manager()
    memory_manager.long_term.store_fact(fact, category)
    return jsonify({"status": "success", "message": "Fact stored"})


@app.route('/api/memory/fact', methods=['GET'])
@require_api_key
def retrieve_facts():
    """Retrieve facts from long-term memory."""
    category = request.args.get('category')
    memory_manager = get_memory_manager()
    facts = memory_manager.long_term.retrieve_facts(category=category)
    return jsonify({"facts": facts})


@app.route('/api/memory/preference', methods=['POST'])
@require_api_key
def store_preference():
    """Store a user preference."""
    data = request.get_json()
    key = data.get('key')
    value = data.get('value')
    
    if not key or value is None:
        return jsonify({"error": "Key and value are required"}), 400
    
    memory_manager = get_memory_manager()
    memory_manager.long_term.store_preference(key, value)
    return jsonify({"status": "success", "message": "Preference stored"})


@app.route('/api/memory/preference/<key>', methods=['GET'])
@require_api_key
def retrieve_preference(key):
    """Retrieve a user preference."""
    memory_manager = get_memory_manager()
    value = memory_manager.long_term.retrieve_preference(key)
    if value is None:
        return jsonify({"error": "Preference not found"}), 404
    return jsonify({"key": key, "value": value})


@app.route('/api/memory/entity', methods=['POST'])
@require_api_key
def store_entity():
    """Store an entity in long-term memory."""
    data = request.get_json()
    entity_name = data.get('entity_name')
    entity_data = data.get('entity_data')
    
    if not entity_name or not entity_data:
        return jsonify({"error": "Entity name and data are required"}), 400
    
    memory_manager = get_memory_manager()
    memory_manager.long_term.store_entity(entity_name, entity_data)
    return jsonify({"status": "success", "message": "Entity stored"})


@app.route('/api/memory/entity/<entity_name>', methods=['GET'])
@require_api_key
def retrieve_entity(entity_name):
    """Retrieve an entity from long-term memory."""
    memory_manager = get_memory_manager()
    entity = memory_manager.long_term.retrieve_entity(entity_name)
    if entity is None:
        return jsonify({"error": "Entity not found"}), 404
    return jsonify({"entity_name": entity_name, "data": entity})


@app.route('/api/memory/search', methods=['GET'])
@require_api_key
def search_memory():
    """Search through long-term memory."""
    query = request.args.get('query')
    if not query:
        return jsonify({"error": "Query parameter is required"}), 400
    
    memory_manager = get_memory_manager()
    results = memory_manager.long_term.search_memory(query)
    return jsonify({"results": results})


# ========== Goals Management Endpoints ==========

@app.route('/api/goals', methods=['POST'])
@require_api_key
def add_goal():
    """Add a new goal."""
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    priority = data.get('priority', 'medium')
    target_date = data.get('target_date')
    
    if not title or not description:
        return jsonify({"error": "Title and description are required"}), 400
    
    memory_manager = get_memory_manager()
    goal = memory_manager.goals.add_goal(title, description, priority, target_date)
    return jsonify({"status": "success", "goal": goal})


@app.route('/api/goals', methods=['GET'])
@require_api_key
def get_goals():
    """Get all active goals."""
    memory_manager = get_memory_manager()
    goals = memory_manager.goals.get_active_goals()
    return jsonify({"goals": goals})


@app.route('/api/goals/<int:goal_id>', methods=['GET'])
@require_api_key
def get_goal(goal_id):
    """Get a specific goal by ID."""
    memory_manager = get_memory_manager()
    goal = memory_manager.goals.get_goal_by_id(goal_id)
    if goal is None:
        return jsonify({"error": "Goal not found"}), 404
    return jsonify({"goal": goal})


@app.route('/api/goals/<int:goal_id>/progress', methods=['PUT'])
@require_api_key
def update_goal_progress(goal_id):
    """Update goal progress."""
    data = request.get_json()
    progress = data.get('progress')
    
    if progress is None:
        return jsonify({"error": "Progress value is required"}), 400
    
    memory_manager = get_memory_manager()
    success = memory_manager.goals.update_goal_progress(goal_id, progress)
    if not success:
        return jsonify({"error": "Goal not found"}), 404
    
    return jsonify({"status": "success", "message": "Progress updated"})


@app.route('/api/goals/<int:goal_id>/complete', methods=['POST'])
@require_api_key
def complete_goal(goal_id):
    """Mark a goal as completed."""
    memory_manager = get_memory_manager()
    success = memory_manager.goals.complete_goal(goal_id)
    if not success:
        return jsonify({"error": "Goal not found"}), 404
    
    return jsonify({"status": "success", "message": "Goal completed"})


@app.route('/api/goals/<int:goal_id>/milestone', methods=['POST'])
@require_api_key
def add_milestone(goal_id):
    """Add a milestone to a goal."""
    data = request.get_json()
    milestone = data.get('milestone')
    
    if not milestone:
        return jsonify({"error": "Milestone description is required"}), 400
    
    memory_manager = get_memory_manager()
    success = memory_manager.goals.add_milestone(goal_id, milestone)
    if not success:
        return jsonify({"error": "Goal not found"}), 404
    
    return jsonify({"status": "success", "message": "Milestone added"})


# ========== Streaming Platform Data Endpoints ==========

@app.route('/api/streaming/platforms', methods=['GET'])
def get_platforms():
    """Get list of all available platforms."""
    streaming_data = get_streaming_data()
    platforms = streaming_data.get_all_platforms()
    return jsonify({"platforms": platforms})


@app.route('/api/streaming/platform/<platform>', methods=['GET'])
def get_platform_data(platform):
    """Get detailed data for a specific platform."""
    streaming_data = get_streaming_data()
    data = streaming_data.get_platform_data(platform)
    if data is None:
        return jsonify({"error": "Platform not found"}), 404
    return jsonify({"platform": platform, "data": data})


@app.route('/api/streaming/earnings', methods=['GET'])
def calculate_earnings():
    """Calculate earnings for a platform and view count."""
    platform = request.args.get('platform')
    views = request.args.get('views', type=int)
    
    if not platform or views is None:
        return jsonify({"error": "Platform and views parameters are required"}), 400
    
    streaming_data = get_streaming_data()
    earnings = streaming_data.calculate_earnings(platform, views)
    return jsonify(earnings)


@app.route('/api/streaming/compare', methods=['GET'])
def compare_platforms():
    """Compare earnings across all platforms."""
    views = request.args.get('views', type=int)
    
    if views is None:
        return jsonify({"error": "Views parameter is required"}), 400
    
    streaming_data = get_streaming_data()
    comparison = streaming_data.compare_platforms(views)
    return jsonify({"comparison": comparison})


@app.route('/api/streaming/subscribers', methods=['GET'])
def calculate_subscribers():
    """Calculate expected subscribers from views."""
    platform = request.args.get('platform')
    views = request.args.get('views', type=int)
    quality = request.args.get('quality', 'average')
    
    if not platform or views is None:
        return jsonify({"error": "Platform and views parameters are required"}), 400
    
    streaming_data = get_streaming_data()
    subscribers = streaming_data.calculate_subscribers_from_views(platform, views, quality)
    return jsonify({
        "platform": platform,
        "views": views,
        "quality": quality,
        "expected_subscribers": subscribers
    })


@app.route('/api/streaming/conversion-rates', methods=['GET'])
def get_conversion_rates():
    """Get conversion rate data."""
    conversion_type = request.args.get('type')
    
    if not conversion_type:
        return jsonify({"error": "Type parameter is required"}), 400
    
    streaming_data = get_streaming_data()
    rates = streaming_data.get_conversion_rates(conversion_type)
    if rates is None:
        return jsonify({"error": "Conversion type not found"}), 404
    
    return jsonify({"type": conversion_type, "rates": rates})


@app.route('/api/streaming/requirements/<platform>', methods=['GET'])
def get_requirements(platform):
    """Get monetization requirements for a platform."""
    streaming_data = get_streaming_data()
    requirements = streaming_data.get_monetization_requirements(platform)
    if requirements is None:
        return jsonify({"error": "Platform not found or no requirements available"}), 404
    
    return jsonify({"platform": platform, "requirements": requirements})


@app.route('/api/streaming/factors/<platform>', methods=['GET'])
def get_factors(platform):
    """Get earning factors for a platform."""
    streaming_data = get_streaming_data()
    factors = streaming_data.get_earning_factors(platform)
    if factors is None:
        return jsonify({"error": "Platform not found or no factors available"}), 404
    
    return jsonify({"platform": platform, "factors": factors})


# ========== Context Endpoints ==========

@app.route('/api/context', methods=['GET'])
@require_api_key
def get_full_context():
    """Get complete context from all memory types."""
    memory_manager = get_memory_manager()
    context = memory_manager.get_full_context()
    return jsonify(context)


# Error handlers
@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({"error": "Endpoint not found"}), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return jsonify({"error": "Internal server error"}), 500


if __name__ == '__main__':
    # Get configuration from environment variables
    host = os.environ.get('API_HOST', '0.0.0.0')
    port = int(os.environ.get('API_PORT', 5000))
    debug = os.environ.get('API_DEBUG', 'False').lower() == 'true'
    
    # Check if API key is configured (don't log the actual key)
    env_key = os.environ.get('AI_GENIE_API_KEY', 'dev-key-change-in-production')
    if env_key == 'dev-key-change-in-production':
        auth_status = "⚠ Using default dev key (change in production!)"
    else:
        auth_status = "✓ Custom key configured"
    
    print(f"Starting AI Live Genie API Server...")
    print(f"Authentication: {auth_status}")
    print(f"Host: {host}")
    print(f"Port: {port}")
    print(f"Debug: {debug}")
    print("\nAPI Documentation: See docs/API_DOCUMENTATION.md")
    
    app.run(host=host, port=port, debug=debug)
