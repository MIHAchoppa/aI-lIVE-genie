#!/usr/bin/env python3
"""
Example of generating training data for fine-tuning.
"""

from ai_live_genie.fine_tuning import TrainingDataGenerator, ModelFineTuner

def main():
    # Generate training data for Twitch
    print("=== Generating Training Data for Twitch ===")
    generator = TrainingDataGenerator(platform="twitch")
    
    examples = generator.generate_training_examples(num_examples=100)
    print(f"Generated {len(examples)} training examples")
    
    # Show a sample example
    if examples:
        print("\nSample Training Example:")
        sample = examples[0]
        for message in sample["messages"]:
            print(f"{message['role'].upper()}: {message['content'][:100]}...")
    
    # Export to JSONL
    output_file = "/tmp/twitch_training_data.jsonl"
    generator.export_jsonl(examples, output_file)
    print(f"\nExported training data to {output_file}")
    
    # Create complete dataset
    dataset = generator.create_fine_tuning_dataset()
    print(f"\nDataset Info:")
    print(f"  Platform: {dataset['platform']}")
    print(f"  Number of examples: {dataset['num_examples']}")
    print(f"  Version: {dataset['metadata']['version']}")
    
    # Validate the data
    is_valid = TrainingDataGenerator.validate_training_data(examples)
    print(f"\nTraining data validation: {'✓ PASSED' if is_valid else '✗ FAILED'}")
    
    # Fine-tuning estimates
    print("\n=== Fine-Tuning Estimates ===")
    fine_tuner = ModelFineTuner(platform="twitch")
    
    estimates = fine_tuner.estimate_training_time(num_examples=len(examples))
    print(f"Number of examples: {estimates['num_examples']}")
    print(f"Total training steps: {estimates['total_steps']}")
    print(f"Estimated time: {estimates['estimated_hours']} hours")
    
    # Create fine-tuning job config
    job_config = fine_tuner.create_fine_tuning_job(
        training_file=output_file,
        validation_file=None
    )
    
    print("\nFine-tuning Job Configuration:")
    print(f"  Base Model: {job_config['model']}")
    print(f"  Training File: {job_config['training_file']}")
    print(f"  Model Suffix: {job_config['suffix']}")
    
    # Generate model card
    print("\n=== Model Card ===")
    model_card = fine_tuner.generate_model_card()
    print(model_card[:500] + "...")
    
    # Test with other platforms
    print("\n=== Generating Data for Multiple Platforms ===")
    platforms = ["youtube", "tiktok", "kick"]
    
    for platform in platforms:
        gen = TrainingDataGenerator(platform=platform)
        examples = gen.generate_training_examples(num_examples=50)
        print(f"{platform.title()}: {len(examples)} examples generated")

if __name__ == "__main__":
    main()
