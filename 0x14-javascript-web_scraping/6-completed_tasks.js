#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode === 200) {
    const todos = JSON.parse(body);
    const completedTasksByUser = {};

    todos.forEach(todo => {
      if (todo.completed) {
        if (completedTasksByUser[todo.userId] === undefined) {
          completedTasksByUser[todo.userId] = 1;
        } else {
          completedTasksByUser[todo.userId]++;
        }
      }
    });

    for (const userId in completedTasksByUser) {
      console.log(`User ${userId} completed ${completedTasksByUser[userId]} tasks.`);
    }
  } else {
    console.error('Failed to fetch URL. Status code:', response.statusCode);
  }
});
