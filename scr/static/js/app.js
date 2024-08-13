// static/js/app.js

$(document).ready(function () {
  // Función para cargar las tareas al cargar la página
  loadTasks();

  // Función para agregar una tarea
  $("#task-form").submit(function (event) {
    event.preventDefault();
    var taskText = $("#task-input").val().trim(); // Eliminar espacios en blanco al principio y al final
    if (taskText === "") {
      alert("Por favor, introduce una tarea válida.");
      return;
    }
    $.ajax({
      url: "/tasks",
      type: "POST",
      contentType: "application/json",
      data: JSON.stringify({ text: taskText }),
      success: function (response) {
        console.log(response); // Imprimir la respuesta del servidor (nueva tarea)
        loadTasks();
        $("#task-input").val("");
      },
    });
  });

  // Función para cargar las tareas
  function loadTasks() {
    $.get("/tasks", function (tasks) {
      $("#task-list").empty();
      tasks.forEach(function (task) {
        var taskElement = $('<div class="task" data-id="' + task.id + '">');
        var checkbox = $('<input type="checkbox" class="task-checkbox">').prop(
          "checked",
          task.completed
        );
        var taskText = $('<span class="task-text">').text(task.text);
        if (task.completed) {
          taskText.addClass("completed");
        }
        var editBtn = $('<button class="edit-btn">Editar</button>');
        var deleteBtn = $('<button class="delete-btn">Eliminar</button>');
        taskElement.append(checkbox, taskText, editBtn, deleteBtn);
        $("#task-list").append(taskElement);
      });
    });
  }
  // Función para marcar una tarea como completada
  $(document).on("change", ".task-checkbox", function () {
    var taskId = $(this).closest(".task").data("id");
    var isCompleted = $(this).prop("checked");
    console.log("Soy el id de la tt", taskId, "soy el booleano", isCompleted);
    $.ajax({
      url: "/tasks/" + taskId,
      type: "PUT",
      contentType: "application/json",
      data: JSON.stringify({ completed: isCompleted }),
      success: function (response) {
        // Actualizar tarea en el frontend si es necesario
        loadTasks();
      },
      error: function (xhr, textStatus, errorThrown) {
        console.error("Error al marcar la tarea como completada:", errorThrown);
        // Aquí puedes agregar manejo de errores, como mostrar un mensaje al usuario
      },
    });
  });

  // Función para editar una tarea
  $(document).on("click", ".edit-btn", function () {
    var taskText = $(this).siblings(".task-text").text();
    var newTaskText = prompt("Editar tarea:", taskText);
    console.log(newTaskText);
    if (newTaskText !== null) {
      // Si el usuario no cancela el prompt
      newTaskText = newTaskText.trim(); // Eliminar espacios en blanco al principio y al final
      if (newTaskText === "") {
        alert("Por favor, introduce una tarea válida.");
        return;
      }
      var taskId = $(this).closest(".task").data("id");
      console.log(taskId);
      $.ajax({
        url: "/tasksText/" + taskId,
        type: "PUT",
        contentType: "application/json",
        data: JSON.stringify({ text: newTaskText }),
        success: function (response) {
          // Actualizar tarea en el frontend si es necesario
          loadTasks();
        },
      });
    }
  });

  // Función para eliminar una tarea
  $(document).on("click", ".delete-btn", function (event) {
    event.stopPropagation(); // Evitar que el evento se propague al contenedor de la tarea
    var taskId = $(this).closest(".task").data("id");
    console.log("Soy el id de la tarea a eliminar", taskId);
    $.ajax({
      url: "/tasks/" + taskId,
      type: "DELETE",
      success: function (response) {
        // Eliminar tarea del frontend
        loadTasks();
      },
      error: function (error) {
        console.log(error);
      },
    });
  });
});
