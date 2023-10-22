

function myFunction(e) {
  e.preventDefault(); // Prevent the form from actually submitting.

  const wordInput = document.getElementById("word");
  const word = wordInput.value;
  console.log('Word is', word);


   axios.post("/get_input/", { word: word })


}




const form = document.getElementById('frm1');
form.addEventListener('submit', myFunction);

