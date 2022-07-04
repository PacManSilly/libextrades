<script setup>
/* eslint-disable */
import { RouterLink } from 'vue-router';
</script>

<template>
    <div>

        <RouterLink
            :to="{name: 'home'}"
            class="text-2xl text-white font-black tracking-wider md:text-4xl"
        >
            LibExTrades
        </RouterLink>

    </div>
</template>