async function addTask(){
const title=document.getElementById('title').value;
const description=document.getElementById('description').value;
await fetch('http://localhost:5000/tasks',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({title,description,status:'pending'})});
loadTasks();
}
async function loadTasks(){
const res=await fetch('http://localhost:5000/tasks');
const data=await res.json();
document.getElementById('tasks').innerHTML=data.map(t=>`<li>${t.title} - ${t.status}</li>`).join('');
}
loadTasks();