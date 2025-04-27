<template>
    <div class="movieList">
      <h1>Movie List</h1>
      <ul>
        <li v-for="movie in movies" :key="movie.id" @click="selectMovie(movie)"
        :class="{ 'selected': selectedMovie === movie }">
          <p>{{ movie.cn_name }}</p>
          <p>{{ movie.en_name }}</p>
        </li>
      </ul>
    </div>
</template>
  
<script setup>
import { defineProps, defineEmits } from 'vue'

// 接收电影数据
const props = defineProps({
  movies: {
    type: Array,
    required: true
  },
  selectedMovie: {
    type: Object,
    required: true
  }
})

// 事件触发电影选择
const emit = defineEmits()

const selectMovie = (movie) => {
  emit('movie-selected', movie) // 通知父组件选中的电影
}
</script>
  
<style scoped>
  .movieList {
    font-weight: 900;
    text-align: center;
    width: 25%;
    height: 80vh;
    overflow-y: auto;
    padding: 10px;
  }
  ul {
    list-style-type: none;
    padding: 0;
  }
  li {
    height: 75px;
    border-radius: 6px;
    padding: 6px;
    margin: 5px 0;
    background-color: #a5e2d7aa;
    cursor: pointer;
  }
  .selected {
    font-weight: 900;
    background: linear-gradient(to right, #8a7cdd, #6ef5af);
    transition: all 0.5s ease;
  }
  li:hover {
    transform: scale(1.03);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
    background-color: #f0f0f0;
    transition: all 0.3s ease;
  }
</style>
  