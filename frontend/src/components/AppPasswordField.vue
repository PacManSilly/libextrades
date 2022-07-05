<script setup>
/* eslint-disable */
import { ref } from 'vue';
import IconEyeCloseVue from './icons/IconEyeClose.vue';
import IconEyeOpenVue from './icons/IconEyeOpen.vue';


// props
const props = defineProps({
  modelValue: { type: String },
  label: { type: String, default: "Password" },
  minlength: { type: Number, default: 8 },
  required: { type: Boolean, default: true },
  placeholder: {type: String, default: "Enter password..."},
});
// emits
const emit = defineEmits(["update:modelValue"]);

// data
const showPassword = ref(false)

</script>

<template>
    <div class="flex flex-col gap-1">

        <label :for="label" class="text-slate-400 text-xs font-normal md:text-sm">
        {{ props.label }}
        </label>

        <div class="relative group">
            <input
                :value="props.modelValue"
                @input="$emit('update:modelValue', $event.target.value)"
                :type="showPassword ? 'text':'password'"
                :name="props.label"
                :id="props.label"
                :required="required"
                :minlength="minlength"
                :placeholder="placeholder"
                class="w-full p-2 bg-slate-100 text-xs text-slate-700 rounded-sm ring-blue-500 ring-offset-2
                ring-offset-slate-900 transition-all duration-150 group-hover:ring-2 focus:ring-2
                focus:outline-none md:p-2 md:text-sm"
            />

            <div class="absolute top-2 right-2 cursor-pointer">
                <button type="button" @click.prevent="showPassword = !showPassword">
                    <IconEyeOpenVue class="bg-slate-100 h-4 w-4 fill-slate-500 hover:fill-slate-900 md:h-5 md:w-5" v-if="showPassword" />
                    <IconEyeCloseVue v-else class="bg-slate-100 h-4 w-4 fill-slate-500 hover:fill-slate-900 md:h-5 md:w-5" />
                </button>
            </div>

        </div>
    </div>
</template>
