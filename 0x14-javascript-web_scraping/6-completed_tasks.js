#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (!error) {
    const todos = JSON.parse(body);
    let itemsCompleted = {};
    todos.forEach((todo) => {
      if (todo.itemsCompleted && itemsCompleted[todo.userId] === undefined) {
        itemsCompleted[todo.userId] = 1;
      } else if (todo.itemsCompleted) {
        itemsCompleted[todo.userId] += 1;
      }
    });
    console.log(itemsCompleted);
  }
});
