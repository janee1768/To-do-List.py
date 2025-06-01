# To-do List Application
tasks = []

print("To-do List Application")

while True:
    print("🔧 Menu:")
    print("1. Add a Task")
    print("2. View Tasks")
    print("3. Delete a Task")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice (1-4): "))

        if choice == 1:
            # Add a Task
            task = input("Enter task to be added: ")
            tasks.append(task)
            print("✅ Task added!")

        elif choice == 2:
            # View Tasks
            if not tasks:
                print("📭 No tasks to display.")
            else:
                print("\n📋 Your Tasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")

        elif choice == 3:
            # Delete a Task
            if not tasks:
                print("⚠️ No tasks available to delete!")
                continue

            print("\n📋 Current Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            try:
                delete_task_num = int(input("Enter the task number to delete: "))
                if 1 <= delete_task_num <= len(tasks):
                    removed_task = tasks.pop(delete_task_num - 1)
                    print(f"🗑️ Task '{removed_task}' deleted successfully!")
                else:
                    print("❌ Invalid task number!")
            except ValueError:
                print("⚠️ Please enter a valid number.")

        elif choice == 4:
            print("👋 Exiting the To-do List Application. Goodbye!")
            break

        else:
            print("❌ Invalid choice! Please enter a number from 1 to 4.")

    except ValueError:
        print("⚠️ Invalid input! Please enter a number.")




