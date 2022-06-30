<script setup>
/* eslint-disable */
import { ref, onMounted } from 'vue';
import AppAccountSideNavVue from '../components/AppAccountSideNav.vue';
import IconHamburger from '../components/icons/IconHamburger.vue';
import AppUserAvatar from '../components/AppUserAvatar.vue';

// data
const menu = ref(false)
const root = ref('')

// methods
const closeMenu = () => {
    if (menu.value == true) {
        menu.value = false;
    }
}

// on mounted hook
onMounted(() => {
    // document.addEventListener("click", closeMenu)
})
</script>

<template>
    <div class="w-full h-full min-h-screen bg-slate-900">

        <div class="w-full h-full flex relative">

            <!-- start of top nav-->
            <div class="absolute top-0 w-full lg:w-auto z-10 lg:right-10">
                <div class="w-11/12 mx-auto py-6 px-4 flex justify-between items-center">
                    <button @click.prevent="menu = true" class="block lg:hidden" type="button">
                        <IconHamburger class="w-10 h-10 fill-slate-600 hover:fill-slate-100" />
                    </button>
                    <button>
                        <AppUserAvatar />
                    </button>
                </div>
            </div>


            <!-- mobile version toggable -->
            <div class="fixed w-9/12 z-10 md:w-5/12 lg:w-3/12">
                <div
                    :class="menu ? 'translate-x-0':'-translate-x-full'"
                    class="flex w-full absolute top-0 bg-slate-800 shadow-2xl transition transform duration-150 lg:hidden">
                    <AppAccountSideNavVue class=""/>
                </div>
                <!-- large screen version -->
                <div class="hidden bg-slate-800 transition transform duration-150 lg:flex">
                    <AppAccountSideNavVue />
                </div>
            </div>

            <!-- start of account main -->
            <div @click="closeMenu" class="fixed right-0 border w-full h-screen lg:w-9/12">
                ss
            </div>
            <!-- start of account main -->


        </div>

    </div>
</template>