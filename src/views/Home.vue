<template>
    <div>
      <Header/>
      <div class="content">
        <MovieDetail :movie="selectedMovie" />
        <MovieList :movies="movies" :selectedMovie="selectedMovie" @movie-selected="updateSelectedMovie" />
      </div>
      <Footer/>
    </div>
</template>
  
<script setup>
import { ref, onMounted } from 'vue'
import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'
import MovieDetail from '@/components/MovieDetail.vue'
import MovieList from '@/components/MovieList.vue'

// 存储电影数据
const movies = ref([])
const selectedMovie = ref(null)

onMounted(async () => {
  const res = await fetch('src/assets/movies.json')
  const data = await res.json()
  movies.value = data
  selectedMovie.value = data[0] // 默认选中第一个电影
})

// 更新选中电影
const updateSelectedMovie = (movie) => {
  selectedMovie.value = movie
}
</script>
  
<style scoped>
* {
  font-family: 'Courier New', Courier, monospace;
}

  .content {
    display: flex;
    flex-direction: row;
  }
</style>
  