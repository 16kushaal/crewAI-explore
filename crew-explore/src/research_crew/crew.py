from crewai import Agent, Crew, Task
from crewai.project import CrewBase, agent, task, crew
from crewai_tools import SerperDevTool
from dotenv import load_dotenv


load_dotenv()

@CrewBase
class ResearchCrew():
    '''Research Crew with Researcher and Writer Agents'''
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],
            tools=[SerperDevTool()],
            verbose=True
        )
    
    @agent
    def writer(self) -> Agent:
        return Agent(
            config=self.agents_config['writer'],
            verbose=True
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task']
        )
    
    @task
    def write_task(self) -> Task:
        return Task(
            config=self.tasks_config['write_task'],
            output_file='output/report.md'
        )
    
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=[self.researcher(), self.writer()],
            tasks=[self.research_task(), self.write_task()],
            verbose=True
        )

if __name__ == "__main__":
    research_crew = ResearchCrew()
    topic = input("Enter the research topic: ")
    research_crew.crew().kickoff(inputs={"topic":f"{topic}"})
