<script setup>
/* eslint-disable */
import { onMounted, ref } from 'vue';
import { useUserStore } from '../stores/user';

// store
const store = useUserStore()

// data
const active = ref(false)
const root = ref('')

// methods
const closeNav = (e) => {
    if (!root.value.contains(e.target)) {
        active.value = false;
    }
}

// on mounted hook
onMounted(() => {
    document.addEventListener("click", closeNav)
})
</script>

<template>
    <div ref="root" class="relative">

        <button
            @click.prevent="active = !active"
            :class="active ? 'ring-2':''"
            class="flex items-center justify-center h-10 w-10 overflow-hidden ring-white ring-offset-2 ring-offset-slate-900 bg-slate-800 rounded-full transition-all duration-150 hover:ring-2">
            <img v-if="store.userData.data" :src="store.userData.data.mugshot" alt="Picture" class="w-full h-full object-cover object-center">
            <p v-else class="font-black text-2xl text-white">S</p>
        </button>

        <transition
            enter-from-class="scale-0 opeacity-0"
            enter-active-class="transition-all duration-150"
            leave-to-class="scale-0 opeacity-0"
            leave-active-class="transition-all duration-150">
            <button @click.prevent="store.signOut" v-if="active" class="absolute w-24 -left-14 top-15 mt-2 p-2 font-mediu bg-slate-100 rounded-sm transition-all duration-150 hover:bg-blue-500 hover:text-slate-100">
                Sign Out
            </button>
        </transition>

    </div>
</template>