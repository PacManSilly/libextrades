<script setup>
import { RouterLink } from "vue-router";
</script>

<template>
  <main class="pl-20">
    <RouterLink :to="{ name: 'signup' }" class="text-xl pr-10 text-white">Sign Up</RouterLink>
    <RouterLink :to="{ name: 'account' }" class="text-2xl text-white">Account</RouterLink>
  </main>
</template>
