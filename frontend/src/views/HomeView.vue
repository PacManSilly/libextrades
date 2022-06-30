<script setup>
import { RouterLink } from "vue-router";
</script>

<template>
  <main>
    <RouterLink :to="{ name: 'signup' }">Sign Up</RouterLink>
    <RouterLink :to="{ name: 'account' }">Account</RouterLink>
  </main>
</template>
