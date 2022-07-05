<script setup>
/* eslint-disable */
import { RouterView } from "vue-router";
import { useUserStore } from "./stores/user";
import IconLogOut from "./components/icons/IconLogOut.vue";
import AppButton from "./components/AppButton.vue";
import IconCloseBig from "./components/icons/IconCloseBig.vue";

// stores
const store = useUserStore()
</script>

<template>
  <div class="w-full h-full bg-slate-900">
    <RouterView />

    <!-- payment modal -->
    <teleport to="body">
      <transition
        enter-from-class="scale-0 opacity-0"
        enter-active-class="transition-all duration-150"
        leave-to-class="scale-0 opacity-0"
        leave-active-class="transition-all duration-150">
        <div v-if="store.userSignOut.modal" class="w-full absolute top-0 z-30 h-screen min-h-[40rem] bg-slate-900/90 backdrop-blur-lg">

          <div class="w-full h-full relative flex items-center justify-center">
              
            <!-- close button -->
            <button @click.prevent="store.userSignOut.modal = false" type="button" class="absolute group top-5 left-5 p-2 rounded transition-all duration-150 hover:bg-slate-800">
                <IconCloseBig class="w-10 h-10 fill-slate-400 group-hover:fill-slate-200" />
            </button>
            
            
            <div class="w-10/12 flex flex-col bg-slate-900 rounded-md overflow-hidden shadow-lg shadow-slate-700/50 lg:w-4/12">
              <div class="flex flex-col p-6 gap-3 md:items-start md:flex-row">
                <div>
                  <IconLogOut class="w-10 h-10 fill-red-600" />
                </div>
                <div class="flex flex-col gap-3">
                  <span class="text-white font-semibold text-lg ">Sign Out</span>
                  <span class="text-slate-500 font-normal">Are you sure you want to sign out?</span>
                </div>

              </div>
      
              <div class="w-full flex gap-2 items-center justify-end p-2 bg-slate-800">
                <div>
                  <button type="button" @click.prevent="store.userSignOut.modal = false" class="px-4 py-1 text-base text-white bg-transparent border border-white rounded-md transition-all duration-150 hover:scale-105">Cancle</button>
                </div>
                <div>
                  <button type="button" @click.prevent="store.signOut()" class="px-4 py-1 text-base text-slate-900 bg-white border rounded-md transition-all duration-150 hover:scale-105">Sign Out</button>
                </div>
              </div>
            </div>

          </div>
        </div>
      </transition>
    </teleport>

  </div>
</template>
