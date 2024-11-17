#!/usr/bin/node

/**
 * Script to print all characters of a Star Wars movie.
 */

const axios = require('axios');

// Function to fetch character name from the given URL
const fetchCharacterName = async (url) => {
  try {
    const response = await axios.get(url);
    return response.data.name;
  } catch (error) {
    console.error(`Error fetching character: ${error.message}`);
    return null;
  }
};

// Main function to fetch and display characters from a Star Wars movie
const main = async () => {
  const args = process.argv.slice(2);

  if (args.length !== 1) {
    console.error('Usage: ./star_wars_characters.js <Movie ID>');
    process.exit(1);
  }

  const movieId = args[0];
  const baseUrl = `https://swapi.dev/api/films/${movieId}/`;

  try {
    // Fetch movie details
    const response = await axios.get(baseUrl);
    const movieData = response.data;

    // Get the list of character URLs
    const characters = movieData.characters;
    if (!characters || characters.length === 0) {
      console.log('No characters found for the specified movie.');
      return;
    }

    // Fetch and print each character's name
    for (const characterUrl of characters) {
      const name = await fetchCharacterName(characterUrl);
      if (name) {
        console.log(name);
      }
    }
  } catch (error) {
    console.error(`Error fetching movie details: ${error.message}`);
  }
};

main();
