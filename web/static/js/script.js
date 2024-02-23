'use strict'

const hamburger = document.querySelector("#hamburger");
const menu = document.querySelector('#menu');

hamburger.addEventListener('click', function () {
    menu.classList.toggle('hidden')
})

// const dataResponse = document.querySelector('#data')
// const submit = document.querySelector('#submit')

// submit.addEventListener('click', function (e) {
//     e.preventDefault()

//     dataResponse.classList.toggle('hidden')
// })