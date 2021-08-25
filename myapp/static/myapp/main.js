    let counter = 2;
    a = {'name-1': '',
 
  }
  function collectData(){
    let form = document.getElementById('form').elements
    for (key in a){
      console.log(form[key].value)
      a[key] = form[key].value
    }
  }
    function onLoad(){
      var mainDiv = document.getElementById('main')
      mainDiv.innerHTML = ''
      for (key in a) {
        newInput = document.createElement('input')
        newLabel = document.createElement('label')
        newInput.name = key;
        newInput.classList.add('form-control')
        newInput.value = a[key];
        newLabel.innerHTML = key;
        newLabel.classList.add('form-label')
        newInput.style.display = 'block';
        mainDiv.appendChild(newLabel)
        mainDiv.appendChild(newInput)
      }
    }
    function toAdd(){
      collectData();
      counter += 1;
      let newName = 'name-'+ counter;
      a[newName] = '';
      console.log(newName, a)
      onLoad();
    }
    onLoad();
