<script setup>
/* eslint-disable */
import IconLoadingVue from "./icons/IconLoading.vue"


// props
const props = defineProps({
    name: {type: String, default: "Submit"},
    loading: {type: Boolean, default: false}
})
</script>

<template>
  <div class="w-full">
    <button
        type="submit"
        :disabled="loading"
        class="w-full p-2 text-center text-sm text-white bg-blue-500 rounded-sm transition-all duration-150 hover:bg-blue-600
        disabled:bg-slate-800 disabled:cursor-wait"
    >
        <div v-if="props.loading" class="w-full flex items-center justify-center">
            <IconLoadingVue class="animate-spin" />
        </div>
        <p v-else class="font-medium text-sm md:text-base">{{props.name}}</p>
    </button>
  </div>
</template>