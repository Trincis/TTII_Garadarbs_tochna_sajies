document.addEventListener('DOMContentLoaded', function () {
const form = document.getElementById('projectForm');
const taskList = document.getElementById('task-list');

function addTask() {
  const taskItem = document.createElement('div');
  taskItem.className = 'task-item';
  taskItem.innerHTML = `
    <input type="text" name="tasks" placeholder="${translations.taskPlaceholder}" required>
    <button type="button" onclick="removeTask(this)">✖</button>
  `;
  taskList.appendChild(taskItem);
}
window.addTask = addTask;

function removeTask(button) {
  const taskItem = button.parentElement;
  taskList.removeChild(taskItem);
}
window.removeTask = removeTask;

form.addEventListener('submit', function (e) {
  const name = document.getElementById('projectName').value.trim();
  const description = document.getElementById('projectDescription').value.trim();
  const tasks = Array.from(taskList.querySelectorAll('input[name="tasks"]'))
                     .map(input => input.value.trim())
                     .filter(Boolean);

  if (!name || !description || tasks.length === 0) {
    e.preventDefault();  // prevent form submission
    alert('Please fill out all fields and add at least one task.');
  }
});

// Add one initial task input on page load
addTask();

});