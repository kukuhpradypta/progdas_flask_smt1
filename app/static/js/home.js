$(document).ready(function () {
  getTask("all");
});

$("#showUpcomingTask").on("change", function () {
  if ($(this).is(":checked")) {
    // Checkbox diaktifkan, tampilkan upcoming tasks
    getTask("upcoming");
  } else {
    // Checkbox dinonaktifkan, tampilkan semua tasks
    getTask("all");
  }
});

$("#priorityFilter").on("change", function () {
  getTask(`priority?priority=` + $(this).val());
});

function getTask(type) {
  // Cek apakah DataTable sudah diinisialisasi sebelumnya
  if ($.fn.DataTable.isDataTable("#homeTable")) {
    // Hancurkan DataTable lama
    $("#homeTable").DataTable().clear().destroy();
  }

  // Inisialisasi ulang DataTable
  const table = $("#homeTable").DataTable({
    ajax: {
      url: `http://127.0.0.1:5555/api/tasks/${type}`,
      dataSrc: function (json) {
        if (json.status === "success") {
          // Transform the data for DataTables
          return json.tasks.map((task, index) => ({
            no: index + 1,
            title: task.title,
            note: task.note,
            category: task.category,
            deadline: new Date(task.deadline).toLocaleDateString(),
            priority: task.priority,
            action: `
              <div class="flex justify-center items-center gap-2">
                <button
                  class="deleteTask bg-rose-500 text-white p-1 rounded-md outline-none"
                  data-task-id="${task.id}"
                >
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="18"
                    viewBox="0 0 24 24"
                  >
                    <path
                      fill="currentColor"
                      d="M19 4h-3.5l-1-1h-5l-1 1H5v2h14M6 19a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2V7H6z"
                    />
                  </svg>
                </button>
              </div>
            `,
          }));
        } else {
          console.error("Unexpected API response:", json);
          return [];
        }
      },
    },
    columns: [
      { data: "no", className: "text-center" },
      { data: "title" },
      { data: "note" },
      { data: "category" },
      { data: "deadline" },
      { data: "priority" },
      { data: "action", className: "text-center" },
    ],
    drawCallback: function () {
      // Tambahkan event listener pada tombol delete setelah tabel selesai dirender
      $(".deleteTask").on("click", function () {
        Swal.fire({
          title: "Are you sure?",
          text: "You won't be able to revert this!",
          icon: "warning",
          showCancelButton: true,
          confirmButtonText: "Yes, delete task",
          cancelButtonText: "Cancel",
          reverseButtons: true,
        }).then((result) => {
          if (result.isConfirmed) {
            const taskId = $(this).data("task-id");
            deleteTask(taskId);
            Swal.fire("Deleted!", "Your task has been deleted.", "success");
          } else if (
            // Read more about handling dismissals
            result.dismiss === Swal.DismissReason.cancel
          ) {
            Swal.fire("Cancelled", "Your task is safe", "error");
          }
        });
      });
    },
  });
}

$(".modal-footer button").on("click", function () {
  // Ambil data dari form
  const title = $("#title").val();
  const note = $("#note").val();
  const category = $("#category").val();
  const deadline = $("#deadline").val();
  const priority = $("#priority").val();

  // Validasi input
  if (
    !title ||
    !deadline ||
    priority === "Select One" ||
    category === "Select One"
  ) {
    alert("Please fill all required fields!");
    return;
  }

  // Data yang akan dikirim ke API
  const taskData = {
    title: title,
    note: note,
    deadline: deadline,
    priority: priority,
    category: category,
  };

  // Hit API
  $.ajax({
    url: "http://127.0.0.1:5555/api/tasks/add",
    method: "POST",
    contentType: "application/json",
    data: JSON.stringify(taskData),
    success: function (response) {
      if (response.status === "success") {
        // alert("Task added successfully!");
        Swal.fire("Success!", "Task added successfully!", "success");

        // Bersihkan form
        $("#title").val("");
        $("#note").val("");
        $("#category").val("Select One");
        $("#deadline").val("");
        $("#priority").val("Select One");

        // Tutup modal
        $("#closeModalTask").click();

        // Refresh DataTable
        getTask("all");
      } else {
        alert("Failed to add task. Please try again.");
      }
    },
    error: function (xhr, status, error) {
      console.error("Error:", error);
      alert("An error occurred while adding the task.");
    },
  });
});

function deleteTask(taskId) {
  // Konfirmasi sebelum menghapus task
  // if (!confirm("Are you sure you want to delete this task?")) {
  //   return;
  // }

  // Kirim request DELETE ke API
  $.ajax({
    url: "http://127.0.0.1:5555/api/tasks/remove",
    method: "DELETE",
    contentType: "application/json",
    data: JSON.stringify({ id: taskId }),
    success: function (response) {
      if (response.status === "success") {
        // alert("Task deleted successfully!");

        // Refresh DataTable
        getTask("all");
      } else {
        alert("Failed to delete task. Please try again.");
      }
    },
    error: function (xhr, status, error) {
      console.error("Error:", error);
      alert("An error occurred while deleting the task.");
    },
  });
}
