import sqlite3

# Connect to the database (or create if it doesn't exist)
conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()

# Create table for tasks
cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        completed INTEGER DEFAULT 0
    )
""")
conn.commit()

def add_task(title):
    """Add a new task"""
    cursor.execute("INSERT INTO tasks (title) VALUES (?)", (title,))
    conn.commit()
    print(f"✅ Task added: {title}")

def view_tasks():
    """View all tasks"""
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    for task in tasks:
        status = "✅" if task[2] else "❌"
        print(f"{task[0]}. {task[1]} - {status}")

def mark_completed(task_id):
    """Mark a task as completed"""
    cursor.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
    conn.commit()
    print(f"🎉 Task {task_id} marked as completed!")

def delete_task(task_id):
    """Delete a task"""
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    print(f"🗑️ Task {task_id} deleted!")

# Simple CLI interface
while True:
    print("\n📌 Task Manager")
    print("1️⃣ Add Task")
    print("2️⃣ View Tasks")
    print("3️⃣ Mark Task Completed")
    print("4️⃣ Delete Task")
    print("5️⃣ Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        title = input("Enter task title: ")
        add_task(title)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        task_id = int(input("Enter task ID to mark complete: "))
        mark_completed(task_id)
    elif choice == "4":
        task_id = int(input("Enter task ID to delete: "))
        delete_task(task_id)
    elif choice == "5":
        print("Exiting... 👋")
        break
    else:
        print("❌ Invalid choice, try again!")

# Close DB connection
conn.close()
