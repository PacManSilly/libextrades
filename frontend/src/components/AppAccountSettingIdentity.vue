<script setup>
/* eslint-disable */
import AppButton from './AppButton.vue';
import IconFileImage from './icons/IconFileImage.vue';
</script>

<template>
    <div class="w-full h-full min-h-full mx-auto">

        <div class="w-full h-full flex flex-col gap-5 md:w-10/12">

            <div class="mb-10 flex flex-col gap-2">
                <h1 class="text-white font-black text-2xl md:text-4xl">Proof of Identity</h1>
                <span class="text-slate-600 text-sm">
                    Due to government requirements, you need to go through a KYC process to verify your identity.
                    Please provide us a valid government issued identification card, for verification.
                </span>
            </div>

            <div class="w-full flex flex-col gap-5">
                <!-- front view -->
                <div class="flex flex-col gap-2">
                    <label for="front" class="text-slate-400 text-xs font-normal md:text-sm">Front View</label>
                    <div class="w-full h-40 flex flex-col gap-2 items-center justify-center rounded-lg border-2 border-dashed border-slate-700 bg-slate-800">
                        <IconFileImage class="w-10 h-10 fill-slate-700" />
                        <input type="file" name="front" id="front" class="transition-all duration-150 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-xs file:font-semibold file:bg-slate-100 file:text-blue-600 hover:file:bg-slate-100 hover:text-slate-100 md:file:text-sm">
                    </div>
                </div>

                <!-- back view -->
                <div class="flex flex-col gap-2">
                    <label for="front" class="text-slate-400 text-xs font-normal md:text-sm">Back View</label>
                    <div class="w-full h-40 flex flex-col gap-2 items-center justify-center rounded-lg border-2 border-dashed border-slate-700 bg-slate-800">
                        <IconFileImage class="w-10 h-10 fill-slate-700" />
                        <input type="file" name="front" id="front" class="transition-all duration-150 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-xs file:font-semibold file:bg-slate-100 file:text-blue-600 hover:file:bg-slate-100 hover:text-slate-100 md:file:text-sm">
                    </div>
                </div>
            </div>

            <div class="w-full flex md:justify-end">
                <AppButton name="Save" class="w-full md:w-1/4" />
            </div>

        </div>

    </div>
</template>