const form = document.getElementById('projectForm');
const taskList = document.getElementById('taskList');
const projectsContainer = document.getElementById('projectsContainer');

function addTask() {
  const taskItem = document.createElement('div');
  taskItem.className = 'task-item';
  taskItem.innerHTML = `
    <input type="text" placeholder="Task description" required>
    <button type="button" onclick="removeTask(this)">✖</button>
  `;
  taskList.appendChild(taskItem);
}

function removeTask(button) {
  const taskItem = button.parentElement;
  taskList.removeChild(taskItem);
}

form.addEventListener('submit', function (e) {
  e.preventDefault();

  const name = document.getElementById('projectName').value.trim();
  const description = document.getElementById('projectDescription').value.trim();
  const tasks = Array.from(taskList.querySelectorAll('input')).map(input => input.value.trim()).filter(val => val);

  if (!name || !description || tasks.length === 0) {
    alert('Please fill out all fields and add at least one task.');
    return;
  }

  // Create project card
  const projectDiv = document.createElement('div');
  projectDiv.className = 'project-card';
  projectDiv.innerHTML = `
    <h3>${name}</h3>
    <p>${description}</p>
    <ul>${tasks.map(task => `<li>${task}</li>`).join('')}</ul>
  `;
  projectsContainer.prepend(projectDiv);

  // Reset form
  form.reset();
  taskList.innerHTML = '';
  addTask(); // re-add initial task field
});

    // Initial task field
addTask();