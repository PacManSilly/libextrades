<script setup>
/* eslint-disable */
// data
const year = new Date().getFullYear()
</script>

<template>
    <div class="w-full h-full flex items-center justify-center p-5">
        <div class="flex gap-2">
            <p class="text-xs text-slate-500 font-semibold md:text-sm">&copy; {{year}} LibExTrades.com.</p>
            <p class="text-xs text-slate-400 font-semibold md:text-sm">All Rights Reserved.</p>
        </div>
    </div>
</template>