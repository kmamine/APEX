import { DropdownOption, PresetData } from '../types';

// Purpose options
export const purposeOptions: DropdownOption[] = [
  { value: 'LinkedIn', label: '💼 LinkedIn', icon: '💼' },
  { value: 'Resume', label: '📄 Resume', icon: '📄' },
  { value: 'Corporate Website', label: '🏢 Corporate Website', icon: '🏢' },
  { value: 'Personal Branding', label: '✨ Personal Branding', icon: '✨' },
  { value: 'Business Card', label: '🎯 Business Card', icon: '🎯' },
  { value: 'Other', label: '📋 Other', icon: '📋' },
];

// Attire options
export const attireOptions: DropdownOption[] = [
  { value: 'Business Formal', label: '👔 Business Formal', icon: '👔' },
  { value: 'Business Casual', label: '👕 Business Casual', icon: '👕' },
  { value: 'Smart Casual', label: '👻 Smart Casual', icon: '👻' },
  { value: 'Creative Professional', label: '🎨 Creative Professional', icon: '🎨' },
  { value: 'Academic', label: '🎓 Academic', icon: '🎓' },
  { value: 'Other', label: '📋 Other', icon: '📋' },
];

// Background options
export const backgroundOptions: DropdownOption[] = [
  { value: 'Corporate Office', label: '🏢 Corporate Office', icon: '🏢' },
  { value: 'Plain Color', label: '🎨 Plain Color', icon: '🎨' },
  { value: 'Outdoor', label: '🌳 Outdoor', icon: '🌳' },
  { value: 'Studio-like', label: '📸 Studio-like', icon: '📸' },
  { value: 'Library/Academic', label: '📚 Library/Academic', icon: '📚' },
  { value: 'Creative Space', label: '🎪 Creative Space', icon: '🎪' },
  { value: 'Other', label: '📋 Other', icon: '📋' },
];

// Vibe options
export const vibeOptions: DropdownOption[] = [
  { value: 'Confident', label: '💪 Confident', icon: '💪' },
  { value: 'Friendly', label: '😊 Friendly', icon: '😊' },
  { value: 'Approachable', label: '🤝 Approachable', icon: '🤝' },
  { value: 'Authoritative', label: '👑 Authoritative', icon: '👑' },
  { value: 'Creative', label: '🎨 Creative', icon: '🎨' },
  { value: 'Sophisticated', label: '🎩 Sophisticated', icon: '🎩' },
  { value: 'Warm', label: '☀️ Warm', icon: '☀️' },
];

// Lighting options
export const lightingOptions: DropdownOption[] = [
  { value: 'Natural Light', label: '☀️ Natural Light', icon: '☀️' },
  { value: 'Studio Lighting', label: '💡 Studio Lighting', icon: '💡' },
  { value: 'Soft Lighting', label: '🕯️ Soft Lighting', icon: '🕯️' },
  { value: 'Dramatic Lighting', label: '🎭 Dramatic Lighting', icon: '🎭' },
  { value: 'Golden Hour', label: '🌅 Golden Hour', icon: '🌅' },
  { value: 'Professional Flash', label: '📸 Professional Flash', icon: '📸' },
];

// Mood options
export const moodOptions: DropdownOption[] = [
  { value: 'Professional', label: '💼 Professional', icon: '💼' },
  { value: 'Casual', label: '😌 Casual', icon: '😌' },
  { value: 'Serious', label: '🧐 Serious', icon: '🧐' },
  { value: 'Energetic', label: '⚡ Energetic', icon: '⚡' },
  { value: 'Calm', label: '😌 Calm', icon: '😌' },
  { value: 'Inspiring', label: '✨ Inspiring', icon: '✨' },
];

// Age range options
export const ageRangeOptions: DropdownOption[] = [
  { value: '20-30', label: '👶 20-30', icon: '👶' },
  { value: '30-40', label: '👨 30-40', icon: '👨' },
  { value: '40-50', label: '👔 40-50', icon: '👔' },
  { value: '50-60', label: '👴 50-60', icon: '👴' },
  { value: '60+', label: '👵 60+', icon: '👵' },
  { value: 'Not Specified', label: '❓ Not Specified', icon: '❓' },
];

// Gender options
export const genderOptions: DropdownOption[] = [
  { value: 'Male', label: '👨 Male', icon: '👨' },
  { value: 'Female', label: '👩 Female', icon: '👩' },
  { value: 'Non-binary', label: '🧑 Non-binary', icon: '🧑' },
  { value: 'Not Specified', label: '❓ Not Specified', icon: '❓' },
];

// Ethnicity options
export const ethnicityOptions: DropdownOption[] = [
  { value: 'Asian', label: '🌏 Asian', icon: '🌏' },
  { value: 'Black', label: '🌍 Black', icon: '🌍' },
  { value: 'Caucasian', label: '🌎 Caucasian', icon: '🌎' },
  { value: 'Hispanic', label: '🌮 Hispanic', icon: '🌮' },
  { value: 'Middle Eastern', label: '🕌 Middle Eastern', icon: '🕌' },
  { value: 'Mixed', label: '🌈 Mixed', icon: '🌈' },
  { value: 'Not Specified', label: '❓ Not Specified', icon: '❓' },
];

// Resolution options
export const resolutionOptions: DropdownOption[] = [
  { value: '1024x1024 (Standard)', label: '📐 1024x1024 (Standard)', icon: '📐' },
  { value: '1536x1024 (Wide)', label: '📏 1536x1024 (Wide)', icon: '📏' },
  { value: '1024x1536 (Portrait)', label: '📱 1024x1536 (Portrait)', icon: '📱' },
  { value: '2048x2048 (High-Res)', label: '🖥️ 2048x2048 (High-Res)', icon: '🖥️' },
];

// Preset configurations
export const presets: Record<string, PresetData> = {
  'LinkedIn Professional': {
    name: 'LinkedIn Professional',
    purpose: 'LinkedIn',
    attire: 'Business Formal',
    background: 'Corporate Office',
    vibe: 'Confident',
    custom_notes: 'Professional headshot optimized for LinkedIn profile. Clean, crisp, and trustworthy appearance.',
    description: 'Perfect for professional networking and career profiles'
  },
  'Creative Portfolio': {
    name: 'Creative Portfolio',
    purpose: 'Personal Branding',
    attire: 'Creative Professional',
    background: 'Creative Space',
    vibe: 'Creative',
    custom_notes: 'Artistic and creative professional portrait showcasing personality and creativity.',
    description: 'Ideal for artists, designers, and creative professionals'
  },
  'Academic Profile': {
    name: 'Academic Profile',
    purpose: 'Resume',
    attire: 'Academic',
    background: 'Library/Academic',
    vibe: 'Sophisticated',
    custom_notes: 'Professional academic portrait suitable for research profiles and institutional websites.',
    description: 'Great for researchers, professors, and academic professionals'
  },
  'Startup Founder': {
    name: 'Startup Founder',
    purpose: 'Personal Branding',
    attire: 'Smart Casual',
    background: 'Plain Color',
    vibe: 'Confident',
    custom_notes: 'Modern entrepreneur portrait combining professionalism with approachable startup culture.',
    description: 'Modern look for entrepreneurs and startup leaders'
  },
  'Executive Portrait': {
    name: 'Executive Portrait',
    purpose: 'Corporate Website',
    attire: 'Business Formal',
    background: 'Corporate Office',
    vibe: 'Authoritative',
    custom_notes: 'High-level executive portrait projecting leadership, authority, and corporate excellence.',
    description: 'High-level corporate portraits for C-suite executives'
  },
};

// Default form values
export const defaultFormValues = {
  purpose: '',
  attire: '',
  background: '',
  vibe: '',
  lighting: 'Professional Flash',
  mood: 'Professional',
  age_range: 'Not Specified',
  gender: 'Not Specified',
  ethnicity: 'Not Specified',
  resolution: '1024x1024 (Standard)',
  custom_notes: '',
  save_profile: true,
};
