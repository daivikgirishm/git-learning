import random
import string
import asyncio
import time
from datetime import datetime

# -------------------------------------------------------
# RANDOM UTILITY FUNCTIONS
# -------------------------------------------------------

def random_string(length=12):
    """Generate a random string."""
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

def random_number_list(n=20):
    """Generate a list of random numbers."""
    return [random.randint(1, 1000) for _ in range(n)]

def random_choice_message():
    """Return a random message."""
    messages = [
        "Processing data...",
        "Loading modules...",
        "Optimizing resources...",
        "Generating output...",
        "Completing tasks...",
        "Analyzing input..."
    ]
    return random.choice(messages)

# -------------------------------------------------------
# OBJECT SYSTEM (CLASSES)
# -------------------------------------------------------

class Task:
    def __init__(self, task_id):
        self.task_id = task_id
        self.status = "pending"
        self.created_at = datetime.now()

    def update_status(self, new_status):
        self.status = new_status

    def summary(self):
        return {
            "task_id": self.task_id,
            "status": self.status,
            "created_at": str(self.created_at)
        }


class TaskManager:
    def __init__(self):
        self.tasks = {}

    def create_task(self):
        task_id = random_string(8)
        task = Task(task_id)
        self.tasks[task_id] = task
        return task

    def list_tasks(self):
        return [task.summary() for task in self.tasks.values()]

    def update_task(self, task_id, status):
        if task_id in self.tasks:
            self.tasks[task_id].update_status(status)
            return True
        return False


# -------------------------------------------------------
# ASYNC RANDOM SIMULATION ENGINE
# -------------------------------------------------------

async def simulate_task(task: Task):
    """Simulate a task that updates its status every few seconds."""
    statuses = ["queued", "running", "processing", "finalizing", "complete"]

    for s in statuses:
        await asyncio.sleep(random.uniform(0.5, 1.5))
        task.update_status(s)
        print(f"[{datetime.now()}] Task {task.task_id}: {s}")

    return task.summary()


async def run_simulation(batch_size=5):
    manager = TaskManager()
    tasks = [manager.create_task() for _ in range(batch_size)]

    print("\n--- Starting Simulation ---\n")
    results = await asyncio.gather(*(simulate_task(task) for task in tasks))

    print("\n--- Simulation Complete ---\n")
    return results


# -------------------------------------------------------
# MAIN EXECUTION
# -------------------------------------------------------

if __name__ == "__main__":
    print("Random String:", random_string())
    print("Random Numbers:", random_number_list())
    print("Message:", random_choice_message())

    print("\nRunning async simulation. Please wait...\n")

    start_time = time.time()
    final_results = asyncio.run(run_simulation(batch_size=3))
    end_time = time.time()

    print("Final Task Results:\n")
    for res in final_results:
        print(res)

    print(f"\nExecution time: {round(end_time - start_time, 2)} seconds")