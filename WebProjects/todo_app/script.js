function addTodo() {
    const todoInput = document.getElementById('todo-input');
    const todoText = todoInput.value.trim();

    if (todoText) {
        const todoList = document.getElementById('todo-list');
        
        const todoItem = document.createElement('li');
        todoItem.className = 'todo-item';

        const span = document.createElement('span');
        span.textContent = todoText;
        span.onclick = () => toggleComplete(todoItem);
        
        const deleteBtn = document.createElement('button');
        deleteBtn.textContent = 'Delete';
        deleteBtn.onclick = () => deleteTask(todoItem);

        todoItem.appendChild(span);
        todoItem.appendChild(deleteBtn);
        todoList.appendChild(todoItem);

        todoInput.value = '';
    }
}

function toggleComplete(todoItem) {
    todoItem.classList.toggle('completed');
}

function deleteTask(todoItem) {
    todoItem.remove();
}