#!/usr/bin/env python3
"""
Test script for knowledge link parsing functions.
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from mcp_server_datahub.utils import parse_institutional_memory, format_knowledge_links


def test_knowledge_links():
    """Test the knowledge link parsing functions."""
    
    # Sample institutionalMemory data (similar to what we got from DataHub)
    sample_memory = {
        "elements": [
            {
                "url": "https://www.notion.so/Engagement-Type-1f5b7b13af5f8046954ec6866dfd417d",
                "label": "Notion Page"
            }
        ]
    }
    
    # Parse the institutional memory
    knowledge_links = parse_institutional_memory(sample_memory)
    
    print("Parsed Knowledge Links:")
    for link in knowledge_links:
        print(f"url: {link['url']}")
        print(f"name: {link['name']}")
        print()
    
    # Format as readable string
    formatted_output = format_knowledge_links(knowledge_links)
    print("Formatted Output:")
    print(formatted_output)
    
    # Test with empty data
    empty_memory = {}
    empty_links = parse_institutional_memory(empty_memory)
    print(f"\nEmpty memory result: {empty_links}")
    
    # Test with malformed data
    malformed_memory = {"elements": [{"url": "https://example.com"}]}  # missing label
    malformed_links = parse_institutional_memory(malformed_memory)
    print(f"Malformed memory result: {malformed_links}")


if __name__ == "__main__":
    test_knowledge_links()
