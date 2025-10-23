"""
Memory Manager for AI Live Genie
Handles conversational memory, long-term memory, and goals tracking.
"""

import json
import os
from datetime import datetime
from typing import List, Dict, Any, Optional


class ConversationalMemory:
    """Manages short-term conversational memory for ongoing interactions."""
    
    def __init__(self, max_history: int = 50):
        self.max_history = max_history
        self.conversation_history: List[Dict[str, Any]] = []
    
    def add_message(self, role: str, content: str, metadata: Optional[Dict[str, Any]] = None):
        """Add a message to conversational memory."""
        message = {
            "role": role,
            "content": content,
            "timestamp": datetime.now().isoformat(),
            "metadata": metadata or {}
        }
        self.conversation_history.append(message)
        
        # Keep only the most recent messages
        if len(self.conversation_history) > self.max_history:
            self.conversation_history = self.conversation_history[-self.max_history:]
    
    def get_history(self, last_n: Optional[int] = None) -> List[Dict[str, Any]]:
        """Retrieve conversation history."""
        if last_n:
            return self.conversation_history[-last_n:]
        return self.conversation_history
    
    def clear(self):
        """Clear conversational memory."""
        self.conversation_history = []
    
    def get_context_summary(self) -> str:
        """Generate a summary of the current conversation context."""
        if not self.conversation_history:
            return "No conversation history."
        
        summary = f"Conversation with {len(self.conversation_history)} messages:\n"
        for msg in self.conversation_history[-5:]:  # Last 5 messages
            summary += f"- [{msg['role']}]: {msg['content'][:50]}...\n"
        return summary


class LongTermMemory:
    """Manages persistent long-term memory storage."""
    
    def __init__(self, storage_path: str = "data/long_term_memory.json"):
        self.storage_path = storage_path
        # Ensure data directory exists
        os.makedirs(os.path.dirname(self.storage_path), exist_ok=True)
        self.memory: Dict[str, Any] = self._load_memory()
    
    def _load_memory(self) -> Dict[str, Any]:
        """Load memory from persistent storage."""
        if os.path.exists(self.storage_path):
            try:
                with open(self.storage_path, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return {"facts": [], "preferences": {}, "entities": {}}
        return {"facts": [], "preferences": {}, "entities": {}}
    
    def _save_memory(self):
        """Save memory to persistent storage."""
        with open(self.storage_path, 'w') as f:
            json.dump(self.memory, f, indent=2)
    
    def store_fact(self, fact: str, category: str = "general"):
        """Store a fact in long-term memory."""
        fact_entry = {
            "content": fact,
            "category": category,
            "timestamp": datetime.now().isoformat()
        }
        self.memory["facts"].append(fact_entry)
        self._save_memory()
    
    def store_preference(self, key: str, value: Any):
        """Store a user preference."""
        self.memory["preferences"][key] = {
            "value": value,
            "timestamp": datetime.now().isoformat()
        }
        self._save_memory()
    
    def store_entity(self, entity_name: str, entity_data: Dict[str, Any]):
        """Store information about an entity (person, place, thing)."""
        self.memory["entities"][entity_name] = {
            "data": entity_data,
            "timestamp": datetime.now().isoformat()
        }
        self._save_memory()
    
    def retrieve_facts(self, category: Optional[str] = None) -> List[Dict[str, Any]]:
        """Retrieve facts, optionally filtered by category."""
        if category:
            return [f for f in self.memory["facts"] if f.get("category") == category]
        return self.memory["facts"]
    
    def retrieve_preference(self, key: str) -> Optional[Any]:
        """Retrieve a stored preference."""
        pref = self.memory["preferences"].get(key)
        return pref["value"] if pref else None
    
    def retrieve_entity(self, entity_name: str) -> Optional[Dict[str, Any]]:
        """Retrieve information about an entity."""
        entity = self.memory["entities"].get(entity_name)
        return entity["data"] if entity else None
    
    def search_memory(self, query: str) -> List[Dict[str, Any]]:
        """Search through long-term memory."""
        results = []
        query_lower = query.lower()
        
        # Search facts
        for fact in self.memory["facts"]:
            if query_lower in fact["content"].lower():
                results.append({"type": "fact", "data": fact})
        
        # Search entities
        for name, entity in self.memory["entities"].items():
            if query_lower in name.lower():
                results.append({"type": "entity", "name": name, "data": entity})
        
        return results


class GoalsManager:
    """Manages user goals and objectives."""
    
    def __init__(self, storage_path: str = "data/goals.json"):
        self.storage_path = storage_path
        # Ensure data directory exists
        os.makedirs(os.path.dirname(self.storage_path), exist_ok=True)
        self.goals: Dict[str, Any] = self._load_goals()
    
    def _load_goals(self) -> Dict[str, Any]:
        """Load goals from persistent storage."""
        if os.path.exists(self.storage_path):
            try:
                with open(self.storage_path, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return {"active_goals": [], "completed_goals": []}
        return {"active_goals": [], "completed_goals": []}
    
    def _save_goals(self):
        """Save goals to persistent storage."""
        with open(self.storage_path, 'w') as f:
            json.dump(self.goals, f, indent=2)
    
    def add_goal(self, title: str, description: str, priority: str = "medium", 
                 target_date: Optional[str] = None):
        """Add a new goal."""
        goal = {
            "id": len(self.goals["active_goals"]) + len(self.goals["completed_goals"]) + 1,
            "title": title,
            "description": description,
            "priority": priority,
            "target_date": target_date,
            "status": "active",
            "progress": 0,
            "created_at": datetime.now().isoformat(),
            "milestones": []
        }
        self.goals["active_goals"].append(goal)
        self._save_goals()
        return goal
    
    def update_goal_progress(self, goal_id: int, progress: int):
        """Update progress on a goal (0-100)."""
        for goal in self.goals["active_goals"]:
            if goal["id"] == goal_id:
                goal["progress"] = min(100, max(0, progress))
                goal["last_updated"] = datetime.now().isoformat()
                self._save_goals()
                return True
        return False
    
    def complete_goal(self, goal_id: int):
        """Mark a goal as completed."""
        for i, goal in enumerate(self.goals["active_goals"]):
            if goal["id"] == goal_id:
                goal["status"] = "completed"
                goal["progress"] = 100
                goal["completed_at"] = datetime.now().isoformat()
                self.goals["completed_goals"].append(goal)
                self.goals["active_goals"].pop(i)
                self._save_goals()
                return True
        return False
    
    def add_milestone(self, goal_id: int, milestone: str):
        """Add a milestone to a goal."""
        for goal in self.goals["active_goals"]:
            if goal["id"] == goal_id:
                goal["milestones"].append({
                    "description": milestone,
                    "achieved": False,
                    "timestamp": datetime.now().isoformat()
                })
                self._save_goals()
                return True
        return False
    
    def get_active_goals(self) -> List[Dict[str, Any]]:
        """Retrieve all active goals."""
        return self.goals["active_goals"]
    
    def get_goal_by_id(self, goal_id: int) -> Optional[Dict[str, Any]]:
        """Retrieve a specific goal by ID."""
        for goal in self.goals["active_goals"]:
            if goal["id"] == goal_id:
                return goal
        for goal in self.goals["completed_goals"]:
            if goal["id"] == goal_id:
                return goal
        return None


class MemoryManager:
    """Main memory manager integrating all memory types."""
    
    def __init__(self, data_dir: str = "./data"):
        os.makedirs(data_dir, exist_ok=True)
        self.conversational = ConversationalMemory()
        self.long_term = LongTermMemory(os.path.join(data_dir, "long_term_memory.json"))
        self.goals = GoalsManager(os.path.join(data_dir, "goals.json"))
    
    def process_interaction(self, user_input: str, assistant_response: str):
        """Process a complete interaction and store in conversational memory."""
        self.conversational.add_message("user", user_input)
        self.conversational.add_message("assistant", assistant_response)
    
    def get_full_context(self) -> Dict[str, Any]:
        """Get complete context from all memory types."""
        return {
            "conversation_history": self.conversational.get_history(last_n=10),
            "recent_facts": self.long_term.retrieve_facts()[-5:],
            "active_goals": self.goals.get_active_goals(),
            "preferences": self.long_term.memory.get("preferences", {})
        }
