<script setup>
/* eslint-disable */
import { useUserStore } from '../stores/user';
import { ref } from 'vue';
import AppInputField from './AppInputField.vue';
import AppButton from './AppButton.vue';

// stores
const store = useUserStore()

// data
const email = ref(null)
const error = ref(null)

// methods
const updateEmail = () => {
    const formData = new FormData()
    if (email.value == store.userData.data.email) error.value = "This is already your email address"
    else {
        localStorage.setItem('libex_email', JSON.stringify(email.value))
        formData.append('email', email.value)
        store.updateMe(formData)
    }
}
</script>

<template>
    <div class="w-full h-full min-h-full mx-auto">

        <form @submit.prevent="updateEmail" class="w-full h-full flex flex-col gap-5 md:w-10/12">

            <div class="text-center mb-10 flex flex-col gap-2">
                <h1 class="text-white font-black text-2xl md:text-4xl">Update Your Email Address</h1>
                <span class="text-slate-400 font-bold text-xs md:text-sm">Changing your email address will automatically log you out.</span>
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

            <div class="w-full flex flex-col gap-1">
                <AppInputField v-model="email" label="Email Address" placeholder="Enter email address..." type="email" :required="true" />
                <span class="text-slate-500 text-sm font-medium">Your current email address: <b>{{store.userData.data.email}}</b></span>
            </div>

            <div class="w-full flex md:justify-end">
                <AppButton name="Update" class="w-full md:w-1/4" :loading="store.profileUpdate.loading" />
            </div>

        </form>

    </div>
</template>