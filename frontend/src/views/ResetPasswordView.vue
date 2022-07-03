<script setup>
/* eslint-disable */
import { ref } from 'vue';
import { RouterLink } from 'vue-router';
import { useHelp } from '../stores/help';
import AppPasswordField from '../components/AppPasswordField.vue';
import AppButton from '../components/AppButton.vue';
import IconLongLeft from '../components/icons/IconLongLeft.vue'
import AppLogo from '../components/AppLogo.vue'

// stores
const store = useHelp()

// props
const props = defineProps({
    uid: {type: String},
    token: {type: String}
})

// datas
const error = ref(null)
const password1 = ref(null)
const password2 = ref(null)

// methods
const resetPassword = () => {
    const data = {
        uid: props.uid,
        token: props.token,
        new_password1: password1.value,
        new_password2: password2.value
    }

    if (password2.value !== password1.value) error.value = "Passwords does not match!"
    else {
        store.resetPassword(data)
        error.value = null
    }
}
</script>

<template>
<div class="w-full h-full min-h-full bg-slate-900">

    <div class="w-9/12 h-full min-h-[30rem] flex flex-col gap-10 py-20 items-center mx-auto md:w-1/2 lg:w-3/12">

        <!-- start of logo and back nav -->
        <div class="w-full flex items-center justify-between">
            <AppLogo />
            <RouterLink :to="{name: 'home'}" class="flex items-center gap-2 group">
                <IconLongLeft class="w-7 h-7 fill-slate-500 group-hover:animate-bounce-h" />
                <p class="text-blue-500 hover:text-blue-600">Home</p>
            </RouterLink>
        </div>

        <!-- start of sign in form  -->
        <div class="w-full flex flex-col gap-10 mt-20">

            <!-- start of header -->
            <header class="flex flex-col gap-2">
                <p class="text-2xl text-white font-black md:text-4xl">Reset your password</p>
            </header>

             <!-- start of handle errors  -->
            <transition
                enter-from-class="-translate-y-5 opacity-0"
                enter-active-class="transitiona-ll duration-150"
                leave-to-class="-translate-y-5 opacity-0"
                leave-active-class="transitiona-ll duration-150">
                <ul v-if="error || store.password.error || store.password.success" class="flex flex-col text-xs list-inside md:text-sm">
                    <li v-if="error || store.password.error" class="text-red-600">{{store.password.error || error}}</li>
                    <li v-else-if="store.password.success" class="text-green-600">{{store.password.success}}</li>
                </ul>
            </transition>

            <form @submit.prevent="resetPassword" class="w-full flex flex-col gap-5 md:gap-10">
                <!-- start of form fields -->
                <div class="flex flex-col gap-4">
                    <AppPasswordField v-model="password1" label="New Password" />
                    <AppPasswordField v-model="password2" label="Confirm Password" />
                </div>

                <!-- start of button -->
                <div class="w-full flex flex-col gap-3 items-center">
                    <div class="w-full">
                        <AppButton name="Reset my password" :loading="store.password.loading" />
                    </div>
                    <div class="flex items-center gap-2 text-xs md:text-sm">
                        <p class="text-xs font-normal text-slate-500">Back to</p>
                        <RouterLink :to="{name: 'signin'}" class="font-bold text-blue-500 transition-all duration-150 hover:text-blue-600">Sign In</RouterLink>
                    </div>
                </div>
            </form>

        </div>
        
    </div>

</div>
</template>
