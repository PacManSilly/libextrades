<script setup>
/* eslint-disable */
import { RouterLink } from 'vue-router';
</script>

<template>
    <div>

        <RouterLink
            :to="{name: 'home'}"
            class="text-2xl text-white font-black tracking-wider md:text-3xl"
        >
            LibExTrades
        </RouterLink>

    </div>
</template>