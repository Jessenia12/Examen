function addTask() {
    const input = document.getElementById('taskInput');
    const task = input.value;

    fetch('/add_task', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ task: task })
    })
    .then(response => response.json())
    .then(data => {
        const list = document.getElementById('taskList');
        const listItem = document.createElement('li');
        listItem.textContent = data.task;
        list.appendChild(listItem);
        input.value = '';
    });
}
