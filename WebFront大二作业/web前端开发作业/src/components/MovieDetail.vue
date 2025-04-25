<template>
    <div class="movieDetail" v-if="movie">
      <div class="info">
        <h1>{{ movie.cn_name }}</h1>
        <p>English Name:{{ movie.en_name }}</p>
        <p>Tags: {{ movie.tags.join(',') }}</p>
        <p>Region: {{ movie.region }}</p>
        <p>Release Time: {{ movie.release_time }}</p>
        <p>Description: {{ movie.description }}</p>
      </div>
      <div class="imgbox">
        <img :src="movie.img" alt="Movie Poster" class="poster">
      </div>
    </div>
</template>
  
<script setup>
import { defineProps } from 'vue'

// 接收父组件传递的选中电影
const props = defineProps({
  movie: {
    type: Object,
    required: true
  }
})
</script>
  
<style scoped>
@import url('https://fonts.googleapis.com/css2?family=ZCOOL+XiaoWei&display=swap');

  .movieDetail {
    font-family: 'ZCOOL XiaoWei', cursive;
    position: relative;
    width: 75%;
    height: 80vh;
    overflow-y: auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  .info {
    line-height: 50px;
  }
  .poster {
    position: absolute;
    top: 25px;
    right: 35px;
    width: 200px;
    border-radius: 5px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
  }
  .poster:hover {
    transform: scale(1.05);
    transition: all 0.5s ease;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
  }
</style>
  