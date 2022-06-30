<script setup>
/* eslint-disable */
import { RouterLink } from 'vue-router';
</script>

<template>
    <div>

        <RouterLink
            :to="{name: 'home'}"
            class="text-lg text-white font-black tracking-wider md:text-2xl"
        >
            LibExTrades
        </RouterLink>

    </div>
</template>