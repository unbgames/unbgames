<template>
    <v-carousel>
        <v-carousel-item
        v-for="(item,i) in items"
        :key="i"
        :src="item.src"
        reverse-transition="fade"
        transition="fade"
        ></v-carousel-item>
    </v-carousel>  
  </template>
  