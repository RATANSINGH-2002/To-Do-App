// function deleteNote(noteId) {
//     fetch("/delete-note", {
//       method: "POST",
//       body: JSON.stringify({ noteId: noteId }),
//     }).then((_res) => {
//       window.location.href = "/";
//     });
//   }

function deleteNote(noteId) {
    console.log("Deleting Note ID:", noteId); // Debugging log

    fetch("/delete-note", {
        method: "POST",
        body: JSON.stringify({ noteId: noteId }),
        headers: { "Content-Type": "application/json" } // Ensure JSON format
    })
    .then(res => {
        if (!res.ok) throw new Error("Failed to delete note");
        return res.json();
    })
    .then(data => {
        console.log("Note deleted successfully");
        window.location.href = "/";
    })
    .catch(err => console.error("Error:", err)); // Handle errors
}
