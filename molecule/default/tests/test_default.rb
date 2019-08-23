# frozen_string_literal: true

describe file('/etc/security/limits.conf') do
  it { should exist }
end

describe limits_conf('/etc/security/limits.conf') do
  its('*') { should include %w[hard nofile 64000] }
  its('*') { should include %w[soft nofile 64000] }
  its('*') { should include %w[hard nproc 64000] }
  its('*') { should include %w[soft nproc 64000] }
  its('*') { should include %w[hard memlock 1024] }
  its('*') { should include %w[soft memlock 1024] }
end
