"""Utility functions for AI Live Genie."""

from typing import Dict, Any, List
import yaml
import json


def save_training_data(data: Dict[str, Any], filepath: str) -> None:
    """
    Save training data to a YAML file.
    
    Args:
        data: Training data to save
        filepath: Path to save the file
    """
    with open(filepath, 'w') as f:
        yaml.dump(data, f, default_flow_style=False)


def load_training_data(filepath: str) -> Dict[str, Any]:
    """
    Load training data from a YAML file.
    
    Args:
        filepath: Path to the YAML file
    
    Returns:
        Loaded training data
    """
    with open(filepath, 'r') as f:
        return yaml.safe_load(f)


def format_conversation_history(
    messages: List[Dict[str, str]],
    max_messages: int = 10
) -> List[Dict[str, str]]:
    """
    Format and limit conversation history for API calls.
    
    Args:
        messages: List of conversation messages
        max_messages: Maximum number of messages to keep
    
    Returns:
        Formatted conversation history
    """
    return messages[-max_messages:] if len(messages) > max_messages else messages


def calculate_engagement_rate(
    interactions: int,
    viewers: int
) -> float:
    """
    Calculate engagement rate for a stream.
    
    Args:
        interactions: Number of interactions (messages, reactions, etc.)
        viewers: Number of viewers
    
    Returns:
        Engagement rate as a percentage
    """
    if viewers == 0:
        return 0.0
    return (interactions / viewers) * 100


def parse_metrics_summary(metrics: Dict[str, Any]) -> str:
    """
    Parse metrics into a human-readable summary.
    
    Args:
        metrics: Dictionary of metrics
    
    Returns:
        Formatted summary string
    """
    summary_lines = ["Stream Metrics Summary:"]
    
    for key, value in metrics.items():
        formatted_key = key.replace('_', ' ').title()
        summary_lines.append(f"  {formatted_key}: {value}")
    
    return "\n".join(summary_lines)
