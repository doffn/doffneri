function addWorkItem(imgSrc, altText, title, description, link) {
  // create a new work item element
  var newItem = document.createElement('div');
  newItem.className = 'work';
  
  // add the data-index attribute
  newItem.setAttribute('data-index', document.querySelectorAll('.work').length + 1);

  // create the image element
  var img = document.createElement('img');
  img.src = imgSrc;
  img.alt = altText;
  newItem.appendChild(img);

  // create the layer element
  var layer = document.createElement('div');
  layer.className = 'layer';
  newItem.appendChild(layer);

  // create the title element
  var h3 = document.createElement('h3');
  h3.textContent = title;
  layer.appendChild(h3);

  // create the description element
  var p = document.createElement('p');
  p.textContent = description;
  layer.appendChild(p);

  // create the link element
  var a = document.createElement('a');
  a.href = link;
  var icon = document.createElement('i');
  icon.className = 'bx bx-link-external';
  a.appendChild(icon);
  layer.appendChild(a);

  // add the new work item to the work list
  var workList = document.querySelector('.work-list');
  workList.appendChild(newItem);
}



// looping through the json file to get the data from the stored data
for (let i = 0; i < myData.length; i++) {
  const { imgSrc, altText, title, description, link } = myData[i];
  
  try {
     // create a new function that calls addWorkItem with the current item's data
     const createWorkItem = function() {
     addWorkItem(imgSrc, altText, title, description, link);
  }
     // call the createWorkItem function to add the current item's data to the work list
     createWorkItem();
  } catch (error) {
     console.log(error);
  }
};


// select the "See more" button
var seeMoreButton = document.querySelector('.btn');
const num = 3; // minimum number of row
// add an event listener to the "See more" button
seeMoreButton.addEventListener('click', function() {
  // toggle between displaying 3 and all work items
  var allItems = document.querySelectorAll('.work');
  var hiddenItems = document.querySelectorAll('.work:not([style="display: block;"])');
  var numToShow = Math.min(hiddenItems.length, num); // show at most 3 items
  if (hiddenItems.length > 0) {
    // display all work items
    for (var i = 0; i < numToShow; i++) {
      hiddenItems[i].style.display = 'block';
    }
  } else {
    // display only 3 work items
    for (var i = 0; i < allItems.length; i++) {
      if (i < num) {
        allItems[i].style.display = 'block';
      } else {
        allItems[i].style.display = 'none';
      }
    }
    seeMoreButton.textContent = 'See more';
  }
  var displayedItems = document.querySelectorAll('.work:not([style="display: none;"])');
  //console.log(displayedItems)
  if (displayedItems.length === allItems.length) {
    seeMoreButton.textContent = 'See Less';
  }
  
});

// display the first 3 work items
var allItems = document.querySelectorAll('.work');
for (var i = 0; i < allItems.length; i++) {
  if (i < 3) {
    allItems[i].style.display = 'block';
  } else {
    allItems[i].style.display = 'none';
  }
}

// hide the "See more" button if there are no hidden work items
var hiddenItems = document.querySelectorAll('.work:not([style="display: block;"])');
if (hiddenItems.length === 0) {
  seeMoreButton.style.display = 'none';
} else {
  seeMoreButton.style.display = 'block';
}



