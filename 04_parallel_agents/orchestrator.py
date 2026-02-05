import threading
import time
import random

def agent_worker(name, task, expertise):
    """
    Simulates an agent performing a task with specific expertise.
    """
    print(f"[{name}] ({expertise}) Acquired task: {task}")
    
    # Simulate thinking/processing time
    duration = random.uniform(1.0, 3.0)
    time.sleep(duration)
    
    print(f"[{name}] Completed '{task}' in {duration:.2f}s")

def orchestration_layer():
    print("--- AntiGravity Parallel Agent Orchestrator ---")
    print("Initializing Agent Swarm...")
    
    tasks = [
        "Analyze Requirements",
        "Design Database Schema",
        "Generate API Endpoints",
        "Write Frontend Components",
        "Run Integration Tests"
    ]
    
    agents = [
        {"name": "Architect-Alpha", "role": "Planning"},
        {"name": "Coder-Beta", "role": "Implementation"},
        {"name": "Tester-Gamma", "role": "QA"}
    ]
    
    threads = []
    
    # Assign tasks to agents in a round-robin fashion
    for i, task in enumerate(tasks):
        agent_info = agents[i % len(agents)]
        t = threading.Thread(
            target=agent_worker, 
            args=(agent_info["name"], task, agent_info["role"])
        )
        threads.append(t)
        t.start()
        
    # Wait for all agents to finish
    for t in threads:
        t.join()
        
    print("--- All parallel tasks completed successfully ---")

if __name__ == "__main__":
    orchestration_layer()
