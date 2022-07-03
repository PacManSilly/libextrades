<script setup>
/* eslint-disable */
import AppButton from './AppButton.vue';
import AppPasswordField from './AppPasswordField.vue';
import { useUserStore } from '../stores/user';
import { ref } from 'vue';

// stores
const store = useUserStore()

// data
const password1 = ref(null)
const password2 = ref(null)
const error = ref(null)

// methods
const updatePassword = () => {
    const data = {
        new_password1: password1.value,
        new_password2: password2.value
    }

    if (password2.value !== password1.value) error.value = "Passwords does not match"
    else {
        error.value = null
        store.changePassword(data)
    }
}
</script>

<template>
    <div class="w-full h-full min-h-full mx-auto">

        <form @submit.prevent="updatePassword" class="w-full h-full flex flex-col gap-5 md:w-10/12">

            <div class="text-center mb-10">
                <h1 class="text-white font-black text-2xl md:text-4xl">Change Your Account Password</h1>
            </div>

            <!-- start of handle errors  -->
            <transition
                enter-from-class="-translate-y-5 opacity-0"
                enter-active-class="transitiona-ll duration-150"
                leave-to-class="-translate-y-5 opacity-0"
                leave-active-class="transitiona-ll duration-150">
                <ul v-if="error || store.profileUpdate.error || store.profileUpdate.success" class="flex flex-col text-xs list-inside md:text-sm">
                    <li v-if="error || store.profileUpdate.error" class="text-red-600">{{store.profileUpdate.error || error}}</li>
                    <li v-else-if="store.profileUpdate.success" class="text-green-600">{{store.profileUpdate.success}}</li>
                </ul>
            </transition>
            
            <div class="w-full flex flex-col gap-5">
                <AppPasswordField v-model="password1" label="New Password" />
                <AppPasswordField v-model="password2" label="Confirm New Password" />
                <span class="text-slate-400 font-bold text-xs md:text-sm">NOTE: Password must be greater than or equals to 8 and contain letters and numbers</span>
            </div>

            <div class="w-full flex md:justify-end">
                <AppButton name="Save" class="w-full md:w-1/4" :loading="store.profileUpdate.loading" />
            </div>

        </form>

    </div>
</template>