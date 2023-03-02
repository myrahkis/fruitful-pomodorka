let gifs = ["https://media.giphy.com/media/QTc4NvhYNlyT7Q32uj/giphy.gif",
            "https://media.giphy.com/media/RoFXqXWN639Qs/giphy.gif",
            "https://media.giphy.com/media/GgrE3sPPZP2us/giphy.gif",
            "https://media.giphy.com/media/J5Vv0RFl0VTEs/giphy.gif",
            "https://media.giphy.com/media/3og0IS3PKTeU9B34MU/giphy-downsized-large.gif",
            ]

function getRandomElement(arr) {
  let randIndex = Math.floor(Math.random() * arr.length);
  return arr[randIndex];
}

let button = document.querySelector('.button');
let image = document.querySelector('.image');

button.addEventListener('click', function () {
    let randomElement = getRandomElement(gifs);
    console.log(randomElement);
    image.src = randomElement;
});

