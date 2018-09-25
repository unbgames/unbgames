var faker = require("faker");

function generateImages(){
    var images = [];
    for (var i = 0, size = 10; i < size; i++) {
        images[i] = {
          src: "http://lorempixel.com/640/480",
          name: faker.name.title(),
          is_gallery: false
        };
    }
    return images;

}

function generateGenres(){
    var genres = []
    for(var i = 0; i < 5; i++){
        genres[i] = faker.name.firstName()
    }
    return genres;
}

function generateAwards(){
    return [
        {
          type_text: "Jogo do ano",
          type: "game_year",
          position: "Primeiro lugar",
          revelation: true
        },
        {
          type_text: "Melhor arte",
          type: "art",
          position: "Primeiro lugar",
          revelation: true
        },
        {
          type_text: "Melhor implementação",
          type: "devel",
          position: "Primeiro lugar",
          revelation: true
        },
        {
          type_text: "Melhor trilha sonora",
          type: "music",
          position: "Primeiro lugar",
          revelation: true
        }
    ]
}

function generatePacks(){
    return [
        {
          platform: "debian",
          link: "http://adah.com",
          architecture: "i386",
          extension: "deb"
        },
        {
          platform: "fedora",
          link: "http://adah.com",
          architecture: "x86_64",
          extension: "rpm"
        },
        {
          platform: "windows",
          link: "http://adah.com",
          architecture: "x86_64",
          extension: "exe"
        },
        {
          platform: "apple",
          link: "http://adah.com",
          architecture: "x86_64",
          extension: "app"
        }
    ]
}


function generateCredits(){
    var credits = []
    var roles = ["Desenvolvedores(as)", "Artistas", "Músicos(as)"]
    for(var i = 0; i < 3; i++){
        credits[i] = {
          role: roles[i],
          authors: [
            {
              name: faker.name.firstName(),
              portifolio: "http://ila.name"
            },
            {
              name: faker.name.firstName(),
              portifolio: "http://ila.name"
            },
            {
              name: faker.name.firstName(),
              portifolio: "http://ila.name"
            }
          ]
        }
    }

    return credits
}

function generateGame(game_id) {
    const game =
        {
            id: game_id,
            name: faker.name.title(),
            year: Math.floor(Math.random() * (2020 - 2000 +1)) + 2000,
            cover_image: "https://raw.githubusercontent.com/unbgames/Wenova/master/res/readme/logo.png",
            description: faker.lorem.paragraph(),
            repository: faker.internet.url(),
            version: 1,
            awards: generateAwards(),
            genres: generateGenres(),
            packs: generatePacks(),
            images: generateImages(),
            //sounds: generateSounds(),
            credits: generateCredits(),
        };
    return game;
}

function generateGamesYear(){
    var games_year = []
    for(var j = 0; j < 5; j++){
        games_year[j] = {
            year: j+2000,
            games: generateGames(j)
        }
    }
    return games_year
}

function generateGames(x){
    var games = []

    for(var i = (x*5); i < 5*(x+1); i++){
        games.push(generateGame(i))
    }
    return games
}

function generateData() {
    return {
        games_year: generateGamesYear(),
        games: generateGames(0)
    };
}

module.exports = generateData;
