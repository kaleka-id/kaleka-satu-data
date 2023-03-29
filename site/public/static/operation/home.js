'use strict'

function getUrlParameter(params){
  const pageUrl = window.location.search.substring(1);
  const urlVariable = pageUrl.split('&');
  for (let i = 0; i < urlVariable.length; i++){
    const parameterName = urlVariable[i].split('=');
    if (parameterName[0] == params){
      return parameterName[1];
    };
  };
};

fetch('/static/operation/testing.json').then((response)=> response.json()).then(
  function(json){
    const listTags = [];
    
    // CREATE STATICTIC CARD
    for(let i = 0; i < json.length; i++){
      const card = document.createElement('div');
      card.setAttribute('class', 'card m-2');
      card.setAttribute('title', json[i].judul);
      card.setAttribute('tags', json[i].tags);
      card.style.width = '18rem';
      card.style.display = 'none';
      card.id = json[i].id

      document.getElementById("data").appendChild(card);
      
      const cardHeader = document.createElement('div');
      cardHeader.classList.add('card-header');
      card.appendChild(cardHeader);
      const cardHeaderBold = document.createElement('b');
      cardHeaderBold.innerHTML = json[i].judul.toUpperCase();
      cardHeader.appendChild(cardHeaderBold);
      
      const cardBody = document.createElement('div');
      cardBody.classList.add('card-body');
      cardBody.innerHTML = `${json[i].nilai} <i>${json[i].satuan}</i>`;
      card.appendChild(cardBody);
      
      const cardFooter = document.createElement('div');
      cardFooter.classList.add('card-footer');
      card.appendChild(cardFooter);
      for(let j = 0; j < json[i].tags.length; j++){
        const span = document.createElement('span');
        span.setAttribute('class', 'badge bg-info text-dark m-1');
        span.innerHTML = json[i].tags[j];
        cardFooter.appendChild(span);
      };

      for(let j = 0; j < json[i].tags.length; j++){
        listTags.push(json[i].tags[j]);
      }

    };
    
    // CREATE FILTER TAGS
    const sortedListTags = [...new Set(listTags)].sort();
    for(let i = 0; i < sortedListTags.length; i++){
      const li = document.createElement('li');
      li.classList.add('dropdown-item');
      li.setAttribute('title', sortedListTags[i]);

      const checkbox = document.createElement('input');
      checkbox.setAttribute('type', 'checkbox');
      checkbox.setAttribute('value', sortedListTags[i]);
      checkbox.classList.add('tag-item');

      const text = document.createElement('text');
      text.innerHTML = ` ${sortedListTags[i]}`;
      
      document.getElementById('tags').appendChild(li);
      li.appendChild(checkbox);
      li.appendChild(text);
    };

    
    // LOGIC TO SHOW CARD
    const card = document.querySelectorAll('.card');
    card.forEach(function(element){
      const tags = document.querySelectorAll('.tag-item');
      const tagItem = element.getAttribute('tags').split(',');
      const tagFilter = (element.title.toUpperCase().includes(getUrlParameter('q').toUpperCase()));
      const tagTotal = tagItem.indexOf('Total') !== -1;
      
      if(tagTotal && tagFilter){
        element.style.display = 'block';
        for(let i = 0; i < tags.length; i++){
          if(tags[i].value.includes('Total')){
            tags[i].checked = true;
          };
        };
      };

      tags.forEach(function(tag){
        tag.addEventListener('change', function(e){
          let tagChecked = e.target.checked;
          let tagValues = tagItem.indexOf(e.target.value) !== -1;
          if(tagFilter && tagChecked && tagValues){
            element.style.display = 'block';
          } else if(tagFilter && !tagChecked && tagValues){
            element.style.display = 'none';
          }
        });
      });  
    });
  },
);


function filterTag() {
  // Declare variables
  let input, filter, ul, li, text, i, txtValue;
  input = document.getElementById('tag-input');
  filter = input.value.toUpperCase();
  ul = document.getElementById('tags');
  li = ul.getElementsByTagName('li');

  // Loop through all list items, and hide those who don't match the search query
  for (i = 0; i < li.length; i++) {
    text = li[i].getElementsByTagName("text")[0];
    txtValue = text.textContent || text.innerText;
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      li[i].style.display = "";
    } else {
      li[i].style.display = "none";
    };
  };
};







// const x = document.getElementsByClassName('card');
// x[0].body.style.backgroundColor="red";
// for(let i = 0; i < x.length; i++){
//   console.log(x[i]);
// }