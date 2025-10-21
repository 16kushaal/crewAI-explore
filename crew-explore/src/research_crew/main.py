import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.research_crew.crew import ResearchCrew

os.makedirs('output', exist_ok=True)

def run():
    """
    Run the research crew.
    """
    topic = input("Enter the research topic: ")
    theinput = {
        'topic': topic
    }

    # Create and run the crew
    result = ResearchCrew().crew().kickoff(inputs=theinput)

    # Print the result
    print("\n\n=== FINAL REPORT ===\n\n")
    print(result.raw)

    print("\n\nReport has been saved to output/report.md")

if __name__ == "__main__":
    run()