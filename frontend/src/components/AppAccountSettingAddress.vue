<script setup>
/* eslint-disable */
import AppInputField from './AppInputField.vue';
import AppButton from './AppButton.vue';

</script>

<template>
    <div class="w-full h-full min-h-full mx-auto">

        <div class="w-full h-full flex flex-col gap-5 md:w-10/12">

            <div class="text-center mb-10">
                <h1 class="text-white font-black text-2xl md:text-4xl">Update Your Address</h1>
            </div>

            <div class="w-full">
                <AppInputField label="Country" />
            </div>

            <div class="w-full grid gap-3 grid-cols-1 md:grid-cols-2">
                <AppInputField label="State" />
                <AppInputField label="City" />
            </div>

            <div class="w-full flex md:justify-end">
                <AppButton name="Save" class="w-full md:w-1/4" />
            </div>

        </div>

    </div>
</template>