<script setup>
/* eslint-disable */
import { computed, onMounted, ref } from 'vue';
import { useUserStore } from '../stores/user';
import IconUser from './icons/IconUser.vue'


// store
const store = useUserStore()

// data
const active = ref(false)
const root = ref('')

// computed 
const isMugshot = computed(() => {
    try {
        return store.userData.data.mugshot
    }
    catch(err) {
        return false
    }
})

const isName = computed(() => {
    try {
        return store.userData.data.first_name
    }
    catch(err) {
        return false
    }
})

// methods
const closeNav = (e) => {
    if (!root.value.contains(e.target)) {
        active.value = false;
    }
}

// hooks
onMounted(() => {
    document.addEventListener("click", closeNav)
})

store.getMe()
</script>

<template>
    <div ref="root" class="relative">

        <button
            @click.prevent="active = !active"
            :class="active ? 'ring-2':''"
            class="flex items-center justify-center h-10 w-10 overflow-hidden ring-blue-600 ring-offset-2 ring-offset-slate-900 rounded-full transition-all duration-150 hover:ring-2">
            <img v-if="isMugshot" :src="store.userData.data.mugshot" alt="Picture" class="w-full h-full object-cover object-center">
            <IconUser v-else class="w-7 h-7 text-slate-400" />
        </button>

        <transition
            enter-from-class="scale-0 opeacity-0"
            enter-active-class="transition-all duration-150"
            leave-to-class="scale-0 opeacity-0"
            leave-active-class="transition-all duration-150">
            <button @click.prevent="store.userSignOut.modal = true" v-if="active" class="absolute w-24 -left-14 top-15 mt-2 p-2 font-mediu bg-slate-100 rounded-sm transition-all duration-150 hover:bg-blue-500 hover:text-slate-100">
                Sign Out
            </button>
        </transition>

    </div>
</template>