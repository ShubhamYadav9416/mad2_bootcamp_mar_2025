<script setup>
import NavBar from '@/components/NavBar.vue';

</script>

<template>
  <header>
    <NavBar></NavBar>

  </header>
  <br>
  <main>
    <div class="container-fluid">
      <div class="row">
        <div class="col-2">
        </div>
        <div class="col" >
          <RouterView></RouterView>

        </div>
        <div class="col-2">
        </div>
      </div>
    </div>
  </main>
</template>

<style scoped>
</style>
